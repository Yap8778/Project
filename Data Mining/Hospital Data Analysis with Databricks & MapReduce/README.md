# 📊 **Hospital Data Analysis with Databricks & MapReduce**

## 📖 **Project Overview**
This project focuses on analyzing large-scale hospital datasets using Databricks for data cleaning and transformation, and MapReduce for distributed processing.  
The analysis provides actionable insights on hospital stay durations, patient health metrics, and departmental process efficiency.

---

## 📂 **Datasets**
- 📄 **Admission** – Admission details including type, admittime, dischtime.  
- 📄 **OMR** – Observation measurements such as weight and height.  
- 📄 **Patient** – Patient demographic details (e.g., gender, subject_id).  
- 📄 **Transfers** – Patient movement between care units with timestamps.  

**Format:** Converted from CSV to Parquet to reduce storage size (~33%) and improve query speed.

---

## 🛠 **Data Processing Workflow**
1. **Data Import & Conversion** – Load CSV datasets and convert to Parquet format.  
2. **Missing Value Handling** – Identify and handle null entries in critical columns.  
3. **Typo Correction** – Use `upper()` and `trim()` to ensure consistent categorical values.  
4. **Data Type Transformation** – Convert timestamps to UNIX format, strings to numeric for calculations.  
5. **Unit Standardization** – Convert weight (lbs → kg) and height (inches → meters).  
6. **Outlier Removal** – Apply IQR method to remove extreme values for accuracy.

---

## 🎯 **Analysis Objectives**
### 1️⃣ Average Hospital Stay by Admission Type
- Extracted and cleaned `admittime`, `dischtime`, and `admission_type`.  
- Calculated stay time in seconds, converted to **HH H MM M SS S** format.  
- Insight: Urgent admissions had significantly longer stays → potential process review needed.

### 2️⃣ Average Height & Weight by Gender
- Joined **OMR** and **Patient** datasets on `subject_id`.  
- Filtered for height and weight, corrected units, removed outliers.  
- Calculated average per patient before group aggregation.  
- Insight: Supports personalized medical planning and early health interventions.

### 3️⃣ MapReduce – Average Process Time by Care Unit & Event Type
- Selected `eventtype`, `careunit`, `intime`, `outtime` from Transfers.  
- Removed irrelevant (`DISCHARGE`) and meaningless (`UNKNOWN`) records.  
- Map Stage: Key = (careunit, eventtype), Value = stay time.  
- Reduce Stage: Aggregated totals, calculated averages, converted to **HH:MM:SS**.  
- Insight: Identifies departments with longer processing times, guiding optimization efforts.

---

## ⚙ **Why MapReduce?**
- Handles **large datasets** (2.4M+ rows) efficiently using disk-based storage.  
- More stable than in-memory Spark when dataset size exceeds available RAM.  
- Produces clear key-value outputs, making results easier to interpret for stakeholders.

---

## 📌 **Conclusion**
By combining Databricks SQL-style processing with MapReduce’s distributed capabilities, this project delivers:  
- Accurate, scalable hospital data analysis.  
- Insights to improve **operational efficiency** and **patient care quality**.  
- A robust framework for handling healthcare datasets that exceed memory limits.
