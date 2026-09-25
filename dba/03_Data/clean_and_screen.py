import pandas as pd

df = pd.read_csv("raw_export_2026-07-22.csv", skiprows=[1, 2])
print(f"Raw rows: {len(df)}")

log = []

def exclude(mask, reason):
    global df
    hit = df[mask]
    for rid in hit["ResponseId"]:
        log.append((rid, reason))
    df = df[~mask]

# --- Order matters: label each exclusion by its *primary* cause. ---

# 1. Researcher test data
exclude(df["Status"] == "Survey Preview", "Survey preview (researcher test)")
exclude(df["OPEN_TEXT"].astype(str).str.strip().str.lower() == "test run", "Self-identified test response")

# 2. Incomplete sessions
exclude(df["Finished"] != True, "Did not finish survey (Finished=False)")

# 3. Finished but substantively empty (blank Likert blocks) — checked BEFORE
#    attention checks so missing data isn't mislabeled as an AC failure.
exclude(df["TA_1"].isna() | df["RAB_5"].isna(), "Finished=True but substantive Likert blocks blank")

# 4. Eligibility screens (as built into the IRB-approved instrument)
exclude(df["S1_COUNTRY"] != "Yes", "Failed screen S1: not US-based")
exclude(df["S2_LANGUAGE"] != "Yes", "Failed screen S2: not fluent English")
exclude(df["S3_AUDIT_ROLE"] != "Yes", "Failed screen S3: no audit-related role in last 24mo")
exclude(df["S4_CONTINUING_ENG"] != "Yes", "Failed screen S4: no continuing (multi-year) engagement experience")
exclude(df["S5_ATTESTATION"] != "Yes, I confirm", "Failed S5 attestation")

# 5. Attention checks (only reached by complete, eligible respondents)
exclude(df["AC1"] != "Disagree", "Failed attention check AC1 (required 'Disagree')")
exclude(~df["AC2"].isin(["Agree", "Strongly agree"]), "Failed attention check AC2 (required 'Agree')")

print(f"\nExcluded: {len(log)}")
for rid, reason in log:
    print(f"  {rid}: {reason}")

print(f"\n=== FINAL VALID N: {len(df)} ===")
print(df[["ResponseId", "RecordedDate", "Duration (in seconds)", "S4_CONTINUING_ENG", "D2_ROLE", "D5_LONGTERM_EXPOSURE"]].to_string())

df.to_csv("cleaned_valid_responses.csv", index=False)

with open("exclusion_log.csv", "w") as f:
    f.write("ResponseId,Reason\n")
    for rid, reason in log:
        f.write(f'{rid},"{reason}"\n')
