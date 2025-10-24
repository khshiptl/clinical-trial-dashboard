import pandas as pd

# Load the dataset
df = pd.read_csv("clinical-trial-dashboard.csv")

# Drop completely empty columns
df = df.dropna(axis=1, how="all")

# Drop duplicate rows
df = df.drop_duplicates()

# Strip leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Remove extra whitespace from string columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Save the cleaned data
df.to_csv("cleaned_clinical_trials.csv", index=False)

print("✅ Data cleaned and saved as cleaned_clinical_trials.csv")
