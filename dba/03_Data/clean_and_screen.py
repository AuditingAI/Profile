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

# 1. Preview / test responses
exclude(df["Status"] == "Survey Preview", "Survey preview (researcher test)")
exclude(df["OPEN_TEXT"].astype(str).str.strip().str.lower() == "test run", "Self-identified test response")

# 2. Incomplete
exclude(df["Finished"] != True, "Did not finish survey (Finished=False)")

# 3. Screening failures
exclude(df["S1_COUNTRY"] != "Yes", "Failed screen: not US-based")
exclude(df["S2_LANGUAGE"] != "Yes", "Failed screen: not fluent English")
exclude(df["S3_AUDIT_ROLE"] != "Yes", "Failed screen: no audit-related role in last 24mo")
exclude(df["S5_ATTESTATION"] != "Yes, I confirm", "Failed attestation")

# 4. Attention checks
exclude(df["AC1"] != "Disagree", "Failed attention check AC1 (expected 'Disagree')")
exclude(~df["AC2"].isin(["Agree", "Strongly agree"]), "Failed attention check AC2 (expected 'Agree')")

# 5. Substantive completeness: require the core Likert blocks to be filled (spot check TA_1 and RAB_5)
exclude(df["TA_1"].isna() | df["RAB_5"].isna(), "Missing substantive Likert data despite Finished=True")

print(f"\nExcluded: {len(log)}")
for rid, reason in log:
    print(f"  {rid}: {reason}")

print(f"\n=== FINAL VALID N: {len(df)} ===")
print(df[["ResponseId", "RecordedDate", "Duration (in seconds)", "OPEN_TEXT"]].to_string())

df.to_csv("cleaned_valid_responses.csv", index=False)

with open("exclusion_log.csv", "w") as f:
    f.write("ResponseId,Reason\n")
    for rid, reason in log:
        f.write(f'{rid},"{reason}"\n')
