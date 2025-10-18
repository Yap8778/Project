# 🩺 **Cirrhosis Patient Survival Prediction using Random Forest**

## 📖 **Project Overview**
This project applies **data mining and machine learning** techniques to predict the survival status of patients with **liver cirrhosis**.  
Using clinical, demographic, and histological data, the goal is to identify key factors influencing patient outcomes and improve predictive accuracy through **feature selection**.

---

## 📂 **Dataset Overview**
- **Source:** [UCI Cirrhosis Patient Survival Prediction Dataset](https://archive.ics.uci.edu/dataset/878/cirrhosis+patient+survival+prediction+dataset-1)
- **Instances:** 418 patients  
- **Attributes:** 20 (ID, clinical indicators, complications, histologic stage)  
- **Target Variable:** `Status` –  
  - C = Censored (alive at study end)  
  - CL = Censored due to liver transplant  
  - D = Death  
- **Example Features:** Age, Sex, Ascites, Hepatomegaly, Platelets, Bilirubin, Stage, etc.

---

## 🛠 **Data Preprocessing**
### 1️⃣ Missing Value Handling
- Removed patients with >45% missing values (mainly missing drug data – MNAR type).
- Imputation strategy:  
  - **Median**: Cholesterol, Triglycerides, Copper (right-skewed distributions)  
  - **Mean**: Platelets (approx. normal distribution)

### 2️⃣ Feature Transformation
- Converted `N_Days` to `Age` in years.
- One-Hot Encoding for categorical variables (e.g., `Sex`, `Drug`, `Status`).

---

## 📊 **Exploratory Data Analysis**
- **Age vs Stage** → Significant difference (p=0.01857) between early (Stage 1–2) and late (Stage 3–4) stages.  
- **Platelets vs Stage** → Lower platelet counts in advanced stages.  
- **Drug Usage Trend** → D-penicillamine more common in early stages; placebo more common later.  
- **Complications vs Stage** → Hepatomegaly & Spiders increase early; Ascites & Edema increase late.

---

## 🤖 **Model Development**
### Algorithm: **Random Forest Classifier**
- Feature selection via **p-value backward elimination**.  
- Two models compared:
  1. **With Feature Selection** – Removed high p-value features (Cholesterol, Platelets, Triglycerides, Spiders).
  2. **Without Feature Selection** – Used all features.

### Parameters:
- `n_estimators`: 500 (feature selection phase), 100 (final model)  
- `max_depth`: 20 (feature selection phase)  
- `class_weight`: "balanced"  
- Train/Test Split: 70/30

---

## 📈 **Results**
| Model | Features Used | Accuracy |
|-------|--------------|----------|
| With Feature Selection | Reduced set | **82.98%** |
| Without Feature Selection | All features | **81.91%** |

**Key Insight:** Even a ~1% accuracy improvement suggests that removing noisy, non-significant features helps model performance and generalization.

---

## ⚙ **Technologies Used**
- 🐍 Python  
- 📦 pandas, numpy, scikit-learn, scipy  
- 📊 matplotlib, seaborn (for visualization)

---

## 🚀 **How to Run**
1. Clone the repository.  
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn scipy matplotlib seaborn
