import pandas as pd


df = pd.read_csv("clinical-trial-dashboard.csv")


df = df.dropna(axis=1, how="all")

df = df.drop_duplicates()

df.columns = df.columns.str.strip()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

df.to_csv("cleaned_clinical_trials.csv", index=False)

print("Data cleaned and saved as cleaned_clinical_trials.csv")
