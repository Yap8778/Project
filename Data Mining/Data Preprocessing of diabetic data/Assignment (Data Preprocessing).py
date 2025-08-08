import pandas as pd

# Set the file path
file_path = r"C:\Users\junso\Documents\DH\SEM 5\Health Data Engineering\diabetic_data.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Show the firts 10 row instances
print("Step 1: Visualize the data in Spyder")
print("Here are the first 10 row instances of the dataset:")
print("----------------------------------------------------------------------------------------------------------")
print(df.head(10))
print("\nHere are the columns name and their data types: ")
print(df.info())

# df.shape [1] will only show the number of columns, while df.shape [0] will show the number of rows
# Print the number of column before drop
print("\nStep 2: Drop the features that are not related to the objective")
print(f"Before drop: {df.shape[1]} columns")

# Create an array to store which column need to be dropped
drop_columns = [
    'encounter_id', 'patient_nbr', 'race', 'gender', 'weight',
    'admission_type_id', 'discharge_disposition_id', 'admission_source_id',
    'time_in_hospital', 'payer_code', 'medical_specialty', 'num_lab_procedures',
    'num_procedures', 'num_medications', 'number_outpatient', 'number_emergency',
    'number_inpatient', 'diag_1', 'diag_2', 'diag_3', 'number_diagnoses',
    'max_glu_serum', 'A1Cresult'
]

# Drop the unnecessary column
df_dropped = df.drop(columns=drop_columns)

# Print the number of column after drop
print(f"After drop: {df_dropped.shape[1]} columns")

# Show the first 10 row instances that already drop the column
print("\nHere are the first 10 row instances of te dataset that already dropped the column:")
print("----------------------------------------------------------------------------------------------------------")
print(df_dropped.head(10))

# Check the remaining column got nan value or not
print("\nStep 3: Check the remaining column got missing value or not")
print("Checking for NaN values in the remaining columns:")
for col in df_dropped.columns:
    nan_count = df_dropped[col].isnull().sum()
    print(f"\nColumn name: {col}")
    print(f"Nan value: {nan_count}")

# Define the medication array
medication_columns = [
    'metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride',
    'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide',
    'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol',
    'troglitazone', 'tolazamide', 'examide', 'citoglipton', 'insulin',
    'glyburide-metformin', 'glipizide-metformin', 'glimepiride-pioglitazone',
    'metformin-rosiglitazone', 'metformin-pioglitazone'
]

# Identify the logic issue: If all medication is 'no', but diabetesMed 'Yes' is not correct
mask_no_med_but_yes_flag = (
    (df_dropped[medication_columns] == 'No').all(axis=1) &
    (df_dropped['diabetesMed'] == 'Yes')
)

# Identify the logic issue: If all medication is 'yes', but diabetesMed 'No' is not correct
mask_med_but_no_flag = (
    (df_dropped[medication_columns] != 'No').any(axis=1) &
    (df_dropped['diabetesMed'] == 'No')
)

# Calculate the result
count_no_med_but_yes = mask_no_med_but_yes_flag.sum()
count_med_but_no = mask_med_but_no_flag.sum()

# Output Result
print("\nStep 4: Identify the logic issue")
print(f"Number of logic issue records (no med but diabetesMed='Yes'): {mask_no_med_but_yes_flag.sum()}")
print(f"Number of logic issue records (med used but diabetesMed='No'): {mask_med_but_no_flag.sum()}")

# Valid medication values
valid_values = {'No', 'Down', 'Steady', 'Up'}

# Check for typos
print("\nStep 5: Check for typos")
print("Checking for typos in medication columns:")
typo_found = False

# unique() is to retrieve the value that exist in entire column
# Example: the column got [Steady, Down, Up, Up, No, Stdhue], so the computer will get [Steady, Down, Up, No, Stdhue]
# Then compare to the valid values to find the typo
for col in medication_columns:
    unique_vals = set(df_dropped[col].unique())
    invalid_vals = unique_vals - valid_values
    if invalid_vals:
        typo_found = True
        print(f"\nColumn name: {col}")
        print(f"Typo values: {invalid_vals}")

if not typo_found:
    print("No typos found in medication columns.")

# Check for typos in change and diabetesMed columns
print("\nChecking for typos in 'change' and 'diabetesMed' columns:")
valid_change = {'No', 'Ch'}
valid_diabetesMed = {'No', 'Yes'}

# Check 'change' column
change_invalid = set(df_dropped['change'].unique()) - valid_change
if change_invalid:
    print(f"Typo in 'change' column: {change_invalid}")

# Check 'diabetesMed' column
diabetesMed_invalid = set(df_dropped['diabetesMed'].unique()) - valid_diabetesMed
if diabetesMed_invalid:
    print(f"Typo in 'diabetesMed' column: {diabetesMed_invalid}")

if not typo_found and not change_invalid and not diabetesMed_invalid:
    print("No typos found in 'change' and 'diabetesMed' columns.")

# Check for typos in 'readmitted' column
print("\nChecking for typos in 'readmitted' column:")
valid_readmitted = {'NO', '<30', '>30'}
readmitted_invalid = set(df_dropped['readmitted'].unique()) - valid_readmitted

if readmitted_invalid:
    print(f"Typo in 'readmitted' column: {readmitted_invalid}")
else:
    print("No typos found in 'readmitted' column.")

# If no typos, proceed to encoding
print("\nStep 6: One hot encoding")
if not typo_found and not change_invalid and not diabetesMed_invalid:
    encoding_map = {'No': 0, 'Down': 1, 'Steady': 2, 'Up': 3}
    change_map = {'No': 0, 'Ch': 1}
    diabetesMed_map = {'No': 0, 'Yes': 1}
    readmission_map = {'NO': 0, '<30': 1, '>30': 1}

    # Create a new DataFrame with original columns and encoded columns
    df_encoded_final = df_dropped.copy()

    # Encoding medication columns
    for col in medication_columns:
        df_encoded_final[f"{col}_encoded"] = df_encoded_final[col].map(encoding_map)

    # Encoding 'change' column
    df_encoded_final['change_encoded'] = df_encoded_final['change'].map(change_map)

    # Encoding 'diabetesMed' column
    df_encoded_final['diabetesMed_encoded'] = df_encoded_final['diabetesMed'].map(diabetesMed_map)
    
    # Encoding 'readmitted' column
    df_encoded_final['readmitted_encoded'] = df_encoded_final['readmitted'].map(readmission_map)

    # Keep only the relevant columns (age, change, diabetesMed, readmitted, and encoded columns)
    encoded_columns = ['age'] + [f"{col}_encoded" for col in medication_columns] + ['change_encoded', 'diabetesMed_encoded', 'readmitted_encoded'] 
    df_encoded_final = df_encoded_final[encoded_columns]
    
    # Display the final encoded DataFrame
    print("\nFinal encoded DataFrame with original and encoded columns:")
    print(df_encoded_final.head())
    print("\nHere are the finalized dataset with the column name and their data type:")
    print(df_encoded_final.info())

# Save the encoded DataFrame as a CSV file
df_encoded_final.to_csv(r"C:\Users\junso\Documents\DH\SEM 5\Health Data Engineering\encoded_diabetic_data.csv", index=False)