# 🩺 **Breast Cancer Diagnosis Prediction with Feature Selection & KNN**

## 📖 **Project Overview**
This project implements **Breast Cancer Wisconsin Diagnostic** dataset classification using **K-Nearest Neighbors (KNN)**.  
It compares three different approaches:  
1. Using all features  
2. Using top 10 features selected by **Mutual Information**  
3. Using top 10 features selected by **P-value (t-test)**  

The workflow includes dataset extraction, preprocessing, feature selection, and model evaluation.

---

## 📂 **Dataset**
- 📄 **Source:** UCI Machine Learning Repository – Breast Cancer Wisconsin (Diagnostic) Dataset  
- 📦 **Rows:** 569  
- 📊 **Features:** 30 numeric features + ID + Diagnosis (M = Malignant, B = Benign)  
- 📌 **Target:** `Diagnosis` (1 = Malignant, 0 = Benign)  
- 💾 **File Path:** `Complete_dataset.csv`  

---

## 🛠 **Workflow**
### 1️⃣ Dataset Extraction (`Extract Dataset.py`)
- Fetched dataset from UCI Repository.  
- Added column headers for ID, Diagnosis, and 30 features.  
- Saved as `Complete_dataset.csv`.  

### 2️⃣ Model 1 – All Features (`KNN model (All Features).py`)
- Used all 30 features.  
- Normalized features with **StandardScaler**.  
- Split into 80% training and 20% testing.  
- Trained **KNN (k=5)**.  
- Saved prediction results to `Prediction_vs_Actual_AllFeatures.csv`.

### 3️⃣ Model 2 – Feature Selection via Mutual Information (`Feature Selection (Mutual Information).py`)
- Calculated **Mutual Information** score for each feature.  
- Selected **top 10 features**.  
- Trained KNN on selected features.  
- Saved results to `Prediction_vs_Actual_MutualInformation.csv`.

### 4️⃣ Model 3 – Feature Selection via P-value (`Feture Selection (P-value).py`)
- Performed **t-test** for each feature between malignant and benign groups.  
- Selected **top 10 features with lowest p-values**.  
- Trained KNN on selected features.  
- Saved results to `Prediction_vs_Actual_SelectedFeatures.csv`.

---

## 📊 **Accuracy Comparison**
| Model | Features Used | Accuracy |
|-------|--------------|----------|
| All Features | 30 | *0.9474* |
| Mutual Information | Top 10 | *0.9649* |
| P-value | Top 10 | *0.9737* |

---

## 📌 **Key Insights**
- Feature selection can reduce dimensionality while maintaining accuracy.  
- Mutual Information and P-value methods select different top features.  
- KNN performance can vary depending on selected features.

---

## ⚙ **Technologies Used**
- 🐍 Python  
- 📦 pandas, numpy, matplotlib, scikit-learn, scipy  
- 📊 UCI Machine Learning Repository  

---

## 📎 **How to Run**
1. Clone the repository.  
2. Install dependencies:  
   ```bash
   pip install pandas numpy matplotlib scikit-learn scipy ucimlrepo
