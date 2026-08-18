# 🏠 House Price Prediction

## 📌 Project Overview

This project is a Machine Learning system for predicting house prices based on property characteristics such as carpet area, number of bathrooms, balconies, floor number, furnishing status, transaction type, ownership, facing direction, and location.

The project includes data preprocessing, exploratory data analysis, machine learning model training, model evaluation, and a Streamlit web application for making house price predictions.

---

## 🎯 Project Objective

The main objective of this project is to build a machine learning model capable of estimating house prices from available property information.

---

## 📊 Dataset

The dataset contains house property listings with information about:

- House price
- Carpet area
- Number of bathrooms
- Number of balconies
- Floor
- Transaction type
- Furnishing status
- Ownership
- Facing direction
- Location

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Converted house prices into numerical values.
2. Converted Carpet Area into square feet.
3. Converted floor information into numerical values.
4. Handled missing numerical values using the median.
5. Handled missing categorical values using `"Unknown"`.
6. Grouped locations into the top 50 most frequent locations.
7. Removed unnecessary and high-missing columns.
8. Applied One-Hot Encoding to categorical features.
9. Applied logarithmic transformation to the target price.

---

## 🔍 Exploratory Data Analysis

Several visualizations were created to understand the dataset:

- Distribution of house prices.
- House price versus carpet area.
- Average house price by location.
- House price by furnishing status.

---

## 🤖 Machine Learning Models

Two regression models were trained:

### Random Forest Regressor

The Random Forest model was trained using:

- 100 trees
- Maximum depth of 20
- Random state of 42

### Linear Regression

Linear Regression was used as a baseline model for comparison.

---

## 📈 Model Evaluation

The models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The Random Forest model performed better than Linear Regression.

Because the dataset contains extreme house prices, an additional evaluation was performed after excluding the highest 1% of test prices.

### Model Results

| Model | R² - Full Test Data | R² - 99% Test Data |
|------|---------------------:|-------------------:|
| Random Forest | 0.0199 | 0.8624 |
| Linear Regression | -0.0685 | 0.2635 |

The Random Forest model achieved the best performance on the 99% test dataset.

---

## 💾 Saved Model

The trained Random Forest model was saved as:

```text
models/house_price.pkl