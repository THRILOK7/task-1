import pandas as pd

# Load the CSV file
df = pd.read_csv(r"C:\Users\vathu\Downloads\cleaned_sample_data.csv")

# Print actual column names in the CSV file
print("🔍 Column names found in your file:")
print(df.columns)

# Rename columns safely (strip spaces and standardize names)
df.columns = df.columns.str.strip().str.title()

# Show the data
print("\n📋 Original Data:")
print(df)

# Standardize CITY
if "City" in df.columns:
    df["City"] = df["City"].str.title().str.strip()

# Standardize GENDER
if "Gender" in df.columns:
    df["Gender"] = df["Gender"].str.title().replace({"M": "Male", "F": "Female"}).str.strip()

# Standardize NAME
if "Name" in df.columns:
    df["Name"] = df["Name"].str.title().str.strip()

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna("Unknown", inplace=True)

# Display cleaned data
print("\n✅ Cleaned Data:")
print(df)

# Save cleaned file
df.to_csv("final_cleaned_data.csv", index=False)
print("\n✅ Cleaned data saved as 'final_cleaned_data.csv'")
