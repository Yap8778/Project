# 📊 **Diabetic Patients Medication & Readmission Analysis**

## 📖 **Project Overview**
This project analyzes the relationship between medication strategies (including medication types, combinations, and change status) and hospital readmission rates among diabetic patients across different age groups.  
The analysis is based on the **diabetic_data.csv** dataset, which contains 101,767 patient records and 50 attributes, including admission details, diagnoses, medication usage, and readmission status.

---

## 📂 **Dataset Information**
- 📄 **File Name:** diabetic_data.csv  
- 📦 **Rows:** 101,767  
- 📊 **Columns:** 50  
- 💾 **File Size:** 18.7 MB  
- 📌 **Content:** Medical records of diabetic patients, covering age groups, medications, diagnoses, hospital admissions, and readmission status.

---

## 🛠 **Data Preprocessing Steps**
1. 🗑 **Column Reduction** – Removed unrelated attributes (e.g., patient ID, race, gender) to focus on medication, age, and readmission factors.
2. 🔍 **Missing Value Check** – Verified and prepared for imputation if needed.
3. ⚠ **Logical Error Detection** – Ensured data consistency (e.g., no patient marked as `diabetesMed=No` while taking medications).
4. 📝 **Spelling & Typo Correction** – Fixed inconsistent categorical values to avoid incorrect grouping.
5. 🔢 **One-Hot Encoding** – Encoded medication usage, change status, diabetesMed, and readmission columns for quantitative analysis.  
   - Readmission `<30` and `>30` both encoded as `1` for analysis.
6. 💾 **Export** – Saved the cleaned dataset as `encoded_diabetic_data.csv`.

---

## 🎯 **Objectives**
1. 💊 Determine the most commonly used medication in each age group.  
2. 📈 Identify age groups with the highest hospital readmission rates.  
3. 🔄 Analyze medication change rates across different age groups.  
4. 🧮 Calculate diabetes medication usage rates in each age group.

---

## 📊 **Implementation**
- **Objective 1** – Grouped data by age and counted usage frequency for each medication.  
- **Objective 2** – Calculated readmission rate = (Total Readmitted Patients ÷ Total Patients) × 100.  
- **Objective 3** – Counted patients with `change_encoded = 1` in each age group.  
- **Objective 4** – Counted patients with `diabetesMed_encoded = 1` and calculated percentage.  

Each objective's results were saved as CSV files:
- `Objective_1.csv`  
- `Objective_2.csv`  
- `Objective_3.csv`  
- `Objective_4.csv`  

---

## 💡 **Reflection**
- Proper preprocessing ensures accuracy in drug usage and readmission statistics.  
- Without correcting typos, medication counts would be split into incorrect categories.  
- Incorrect readmission encoding could lead to wrong identification of high-risk age groups.  
- Missing values and logical errors, if unhandled, would distort medication change and usage rates, affecting medical decisions and drug supply strategies.  

---
