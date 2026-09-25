import pandas as pd

df = pd.read_csv("cleaned_valid_responses.csv")
LIKERT = {"Strongly disagree":1,"Disagree":2,"Neither agree nor disagree":3,"Agree":4,"Strongly agree":5}
CONSTRUCTS = ["TA","RA","AT","SAP","FR","IR","RPG","PMI","AJQ","APR","RAB"]

out = pd.DataFrame()
out["ResponseId"] = df["ResponseId"]
for code in CONSTRUCTS:
    for i in range(1,6):
        col = f"{code}_{i}"
        vals = df[col].map(LIKERT)
        if i == 4:  # reverse-coded item
            vals = 6 - vals
            out[f"{code}_{i}r"] = vals
        else:
            out[col] = vals

out.to_csv("cleaned_numeric_recoded.csv", index=False)
print(f"Wrote cleaned_numeric_recoded.csv: {out.shape[0]} rows x {out.shape[1]} cols")
print("Item 4 of each construct is already reverse-coded (suffix 'r'). Load straight into Jamovi.")
