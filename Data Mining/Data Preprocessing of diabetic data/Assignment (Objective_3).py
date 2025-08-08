import pandas as pd

# Set the file path
file_path = r"C:\Users\junso\Documents\DH\SEM 5\Health Data Engineering\encoded_diabetic_data.csv"

# Load dataset
df = pd.read_csv(file_path)

# Function to compute counts + proportions for each age group
def compute_med_change_by_age(group_df, age_group):
    total_patients = len(group_df)
    change_count = (group_df['change_encoded'] == 1).sum()
    change_proportion = (change_count / total_patients) * 100 if total_patients > 0 else 0
    
    return {
        'Age Group': age_group,
        'Total Patients': total_patients,
        'Medication Change Count': change_count,
        'Medication Change %': round(change_proportion, 2)
    }

# Loop through each age group
records = []
for age_group in sorted(df['age'].unique()):
    group_df = df[df['age'] == age_group]
    result = compute_med_change_by_age(group_df, age_group)
    records.append(result)

# Create dataframe
result_df = pd.DataFrame(records)

# Show the result
print("\nMedication change rate in different age group:")
print(result_df.to_string(index=False))

# Save CSV
output_csv = r"C:\Users\junso\Documents\DH\SEM 5\Health Data Engineering\Objective_3.csv"
result_df.to_csv(output_csv, index=False)

print(f"\nFile saved at: {output_csv}")


