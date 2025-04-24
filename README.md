
# 🌾 Crop Production Prediction Using Machine Learning

## 📌 Project Overview

This project focuses on predicting the **total crop production (in tons)** for various crops across different regions and years using machine learning techniques. It aims to support agricultural decision-making by providing accurate forecasts based on historical agricultural data.

---

## 🎯 Problem Statement

Accurate crop production prediction is essential for:

- ✅ Ensuring **food security** and avoiding shortages.
- ✅ Supporting **agricultural policy** decisions (e.g. subsidies, insurance).
- ✅ Optimizing **supply chains** (storage, transportation, market planning).
- ✅ Helping **farmers and agri-tech firms** in decision-making and crop selection.

---

## 🧠 Features

- 📋 Cleaned and preprocessed agricultural dataset (FAOSTAT).
- 📊 Exploratory Data Analysis (EDA) on:
  - Crop & Region-wise productivity.
  - Year-wise trends.
  - Yield and production efficiency.
- 🤖 Regression Models:
  - Linear Regression (baseline)
  - RandomForest Regressor (primary model with high accuracy)
- 📈 Evaluation Metrics:
  - RMSE, MAE, R² Score
- 🌐 **Streamlit App**:
  - User selects **Crop, Region, Area Harvested, Yield, Year**
  - Predicts expected **Production in tons**
  - Easy to use and deployable locally or on the web

---

## 🛠️ Technologies Used

- Python (Pandas, Numpy)
- Scikit-learn (ML models and preprocessing)
- Streamlit (Interactive web app)
- Matplotlib / Seaborn (Data Visualization)
- Pickle (Model serialization)
- Scipy (Winsorization for outliers)

---

## 🗂️ Project Structure

```
Crop-Production-Prediction/
│
├── data/
│   └── final_cleaned_crop_data.csv
│
├── models/
│   ├── random_forest_model.pkl
│   ├── item_encoder.pkl
│   └── area_encoder.pkl
│
├── notebooks/
│   └── crop_production_eda_and_model.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 How to Run the Project

1. **Clone the repo**  
```bash
git clone https://github.com/your-username/Crop-Production-Prediction.git
cd Crop-Production-Prediction
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Run the app**  
```bash
streamlit run app.py
```

---

## 📊 Example Prediction

> **Crop**: Almonds, in shell  
> **Region**: Afghanistan  
> **Year**: 2022  
> **Area Harvested**: 36,000 ha  
> **Yield**: 1,740 kg/ha  
> 🔮 **Predicted Production**: ~63,500 tons

---

## 🙋‍♂️ Developed By

**Tanishq**  
Data Science Capstone Project  

---
