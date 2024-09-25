
import pandas as pd

# Upload the dataset
file_path = "C:/Users/Acer/Downloads/rawdataset/credit_card_transactions.csv"

# Load the dataset into a DataFrame
df = pd.read_csv(file_path)

# Displaying first few rows
print(df.head())


# Get dataframe shapes
print('Shape of creditcard dataframe:', df.shape)


# Get train data info: count, feature names, data types, missing data counts
print('------------------ creditcard Dataframe info------------------')
print(df.info())

# Get statistical summaries for each feature
print('------------------creditcard Dataframe describe------------------')
print(df.describe())

# Check for duplicate rows
duplicates = df.duplicated()

# Count of duplicate rows
duplicate_count = duplicates.sum()
print(f'Number of duplicate rows: {duplicate_count}')

# Optional: Remove duplicate rows
df = df.drop_duplicates()

# Next, Extracting values from the 924,850th index to the end
df_cut = df.iloc[924850:]

# Resetting Index
df_cut.reset_index(drop=True, inplace=True)

print(df_cut.head())

## Dropping the last column
df_cut = df_cut.drop(df_cut.columns[-1], axis=1)

# Checking if the column is actually removed
print(df_cut.head())

# Ensure the dob column is in datetime format
df_cut['dob'] = pd.to_datetime(df_cut['dob'])

reference_date = pd.to_datetime('2020-12-31')

# Calculate the age
df_cut['age'] = (reference_date - df_cut['dob']).dt.days // 365.25

print(df_cut[['dob', 'age']].head())

# Identify missing data
print("Missing data:\n", df_cut.isnull().sum())

# Display unique job titles in the 'job' column
unique_jobs = df_cut['job'].unique()

# Print the unique job titles
print(unique_jobs)




