# 🗳 **Congressional Voting Records Classification with Chi-Square Feature Selection & KNN**

## 📖 **Project Overview**
This project uses the **Congressional Voting Records** dataset to classify members of the U.S. Congress as **Republican** or **Democrat** based on their voting patterns.  
It applies **Chi-Square feature selection** to identify the most influential votes and compares the classification performance of **K-Nearest Neighbors (KNN)** using:
1. Top 10 Chi-Square selected features  
2. All available features

---

## 📂 **Dataset**
- 📄 **Source:** UCI Machine Learning Repository – Congressional Voting Records Dataset  
- 📦 **Rows:** 435  
- 📊 **Features:** 16 binary voting records (`y` = Yes, `n` = No) + Target (Republican/Democrat)  
- 📌 **Target:** `Target` (1 = Republican, 0 = Democrat)  
- 💾 **File Path:** `dataset.csv`  

---

## 🛠 **Workflow**
### 1️⃣ Data Preprocessing
- Missing values (`?`) replaced with the **mode** of each column.  
- Encoded:
  - `Target`: Republican → 1, Democrat → 0  
  - Votes: `y` → 1, `n` → 0  
- Saved cleaned dataset as `Complete_dataset.csv`.

### 2️⃣ Feature Scaling
- Applied **MinMaxScaler** to normalize feature values to the range [0, 1].

### 3️⃣ Chi-Square Feature Selection
- Performed **Chi-Square test** on all features.  
- Selected **Top 10 features** with the highest Chi-Square scores.  
- Saved all feature scores to `chisquare_score.csv`.

### 4️⃣ Model Training – KNN
- Trained **KNN classifier (k=5)** on:
  1. Top 10 Chi-Square selected features  
  2. All features  
- Compared classification accuracy.

---

## 📊 **Results**
| Model | Features Used | Accuracy |
|-------|--------------|----------|
| KNN + Chi-Square | Top 10 features | *0.9310* |
| KNN (All Features) | All 16 features | *0.9080* |

---

## 📌 **Key Insights**
- Chi-Square feature selection identifies the most influential voting patterns for party classification.  
- Using fewer but more relevant features can maintain or improve classification performance while reducing computation time.

---

## ⚙ **Technologies Used**
- 🐍 Python  
- 📦 pandas, numpy, scikit-learn  

---

## 📎 **How to Run**
1. Clone the repository.  
2. Install dependencies:  
   ```bash
   pip install pandas numpy scikit-learn
