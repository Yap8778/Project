import pandas as pd

# Set the file path
file_path = r"C:\Users\junso\Documents\DH\SEM 5\Health Data Engineering\encoded_diabetic_data.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Count total readmission per age group (readmitted = 1)
# groupby () is to contains record of each same age group patients in the same age group
# size() is to count how many rows there are in each group
readmission_counts = (
    df[df['readmitted_encoded'] == 1].groupby('age').size().reset_index(name='Total Readmission')
)

# Count total patients per age group (readmitted = 1 + 0)
total_counts = (
    df.groupby('age').size().reset_index(name='Total Patients')
)

# Merge both counts
merged_df = pd.merge(readmission_counts, total_counts, on='age')

# Calculate readmission rate
merged_df['Readmission Rate (%)'] = round((merged_df['Total Readmission'] / merged_df['Total Patients']) * 100, 2)

# Rename age column for consistency
merged_df = merged_df.rename(columns={'age': 'Age Group'})

# Show the result
print("\nDifferent age group with their readmission rate:")
print(merged_df.to_string(index=False))

# Save as CSV
output_csv = r"C:\Users\junso\Documents\DH\SEM 5\Health Data Engineering\Objective_2.csv"
merged_df.to_csv(output_csv, index=False)

print(f"File saved at: {output_csv}")


