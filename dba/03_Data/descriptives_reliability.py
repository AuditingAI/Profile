import pandas as pd
import numpy as np

df = pd.read_csv("cleaned_valid_responses.csv")
print(f"n = {len(df)}")

LIKERT_MAP = {
    "Strongly disagree": 1, "Disagree": 2, "Neither agree nor disagree": 3,
    "Agree": 4, "Strongly agree": 5,
}

CONSTRUCTS = {
    "TA": "Training and Awareness",
    "RA": "Rotation of Auditors",
    "AT": "Use of Analytical Tools",
    "SAP": "Structured Auditing Processes",
    "FR": "Feedback and Reflection",
    "IR": "Independent Reviews",
    "RPG": "Regulatory and Professional Guidance",
    "PMI": "Performance Metrics and Incentives",
    "AJQ": "Auditor Judgment Quality",
    "APR": "Audit Process Rigor",
    "RAB": "Reduction in Anchoring Bias",
}
REVERSE_ITEM = 4  # item _4 in each construct is reverse-worded, per instrument design

# Build numeric, reverse-coded item matrix
items = {}
for code in CONSTRUCTS:
    for i in range(1, 6):
        col = f"{code}_{i}"
        vals = df[col].map(LIKERT_MAP)
        if i == REVERSE_ITEM:
            vals = 6 - vals
        items[col] = vals
items_df = pd.DataFrame(items)

def cronbach_alpha(item_matrix):
    k = item_matrix.shape[1]
    item_vars = item_matrix.var(axis=0, ddof=1)
    total_var = item_matrix.sum(axis=1).var(ddof=1)
    if total_var == 0 or k < 2:
        return np.nan
    return (k / (k - 1)) * (1 - item_vars.sum() / total_var)

print("\n=== CONSTRUCT-LEVEL DESCRIPTIVES (n=4, reverse-coded, 1-5 scale) ===")
print(f"{'Code':<5}{'Construct':<40}{'Mean':>7}{'SD':>7}{'Min':>6}{'Max':>6}{'Alpha':>8}")
results = []
for code, label in CONSTRUCTS.items():
    cols = [f"{code}_{i}" for i in range(1, 6)]
    sub = items_df[cols]
    construct_score = sub.mean(axis=1)
    alpha = cronbach_alpha(sub)
    row = dict(code=code, label=label, mean=construct_score.mean(), sd=construct_score.std(ddof=1),
               min=construct_score.min(), max=construct_score.max(), alpha=alpha)
    results.append(row)
    print(f"{code:<5}{label:<40}{row['mean']:>7.2f}{row['sd']:>7.2f}{row['min']:>6.2f}{row['max']:>6.2f}{alpha:>8.2f}")

res_df = pd.DataFrame(results)
res_df.to_csv("construct_descriptives_reliability.csv", index=False)

print("\n=== ITEM-LEVEL RESPONSES (reverse-coded, per respondent) ===")
print(items_df.to_string())

print("\n=== RESPONDENT-LEVEL DEMOGRAPHICS (for methods section) ===")
demo_cols = ["D1A_EXT_EXP", "D1B_INT_EXP", "D2_ROLE", "D3_FIRM_TYPE", "D3B_FIRM_SIZE",
             "D4_INDUSTRY", "D5_LONGTERM_EXPOSURE", "D6_CREDENTIAL", "D7_REGION"]
print(df[demo_cols].to_string())
