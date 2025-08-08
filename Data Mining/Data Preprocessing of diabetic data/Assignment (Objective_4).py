import pandas as pd

# Set the file path
file_path = r"C:\Users\junso\Documents\DH\SEM 5\Health Data Engineering\encoded_diabetic_data.csv"

# Load dataset
df = pd.read_csv(file_path)

# Function to compute counts + proportions for each age group
def compute_diabetesmed_by_age(group_df, age_group):
    total_patients = len(group_df)
    diabetesmed_count = (group_df['diabetesMed_encoded'] == 1).sum()
    diabetesmed_proportion = (diabetesmed_count / total_patients) * 100 if total_patients > 0 else 0
    
    return {
        'Age Group': age_group,
        'Total Patients': total_patients,
        'Diabetes Medication Count': diabetesmed_count,
        'Diabetes Medication %': round(diabetesmed_proportion, 2)
    }

# Loop through each age group
records = []
for age_group in sorted(df['age'].unique()):
    group_df = df[df['age'] == age_group]
    result = compute_diabetesmed_by_age(group_df, age_group)
    records.append(result)

# Create dataframe
result_df = pd.DataFrame(records)

# Show the result
print("\nDiabetes medication usage rate in different age groups:")
print(result_df.to_string(index=False))

# Save CSV
output_csv = r"C:\Users\junso\Documents\DH\SEM 5\Health Data Engineering\Objective_4.csv"
result_df.to_csv(output_csv, index=False)

print(f"\nFile saved at: {output_csv}")


