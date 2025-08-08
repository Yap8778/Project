import pandas as pd

# Set the file path
file_path = r"C:\Users\junso\Documents\DH\SEM 5\Health Data Engineering\encoded_diabetic_data.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Drop the unrelated column
df_filtered = df.drop(columns=['change_encoded', 'diabetesMed_encoded', 'readmitted_encoded'])

# Medication columns
medication_columns = [
    'metformin_encoded', 'repaglinide_encoded', 'nateglinide_encoded', 'chlorpropamide_encoded',
    'glimepiride_encoded', 'acetohexamide_encoded', 'glipizide_encoded', 'glyburide_encoded',
    'tolbutamide_encoded', 'pioglitazone_encoded', 'rosiglitazone_encoded', 'acarbose_encoded',
    'miglitol_encoded', 'troglitazone_encoded', 'tolazamide_encoded', 'examide_encoded',
    'citoglipton_encoded', 'insulin_encoded',
    'glyburide-metformin_encoded', 'glipizide-metformin_encoded', 'glimepiride-pioglitazone_encoded',
    'metformin-rosiglitazone_encoded', 'metformin-pioglitazone_encoded'
]

# Calculate the medication counts (both readmission = 0 and 1)
records = []
for age_group in sorted(df_filtered['age'].unique()):
    group_df = df_filtered[df_filtered['age'] == age_group]
    med_counts = (group_df[medication_columns] != 0).sum().to_dict()
    med_counts['Age Group'] = age_group
    records.append(med_counts)

# Create dataframe
medication_counts_df = pd.DataFrame(records)

# Reorder columns so Age Group is first
cols = ['Age Group'] + [col for col in medication_counts_df.columns if col != 'Age Group']
medication_counts_df = medication_counts_df[cols]

# Show the result
print("\nEach medication usage in different age group:")
print(medication_counts_df.to_string(index=False))

# Save as CSV
output_csv = r"C:\Users\junso\Documents\DH\SEM 5\Health Data Engineering\Objective_1.csv"
medication_counts_df.to_csv(output_csv, index=False)

print(f"File saved at: {output_csv}")




