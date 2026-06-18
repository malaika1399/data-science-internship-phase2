# data-science-internship-phase2

# Term Deposit Subscription Prediction

## Objective
Predict whether a bank customer will subscribe to a term deposit using classification models, and explain predictions using SHAP.

## Dataset
Bank Marketing Dataset (UCI Machine Learning Repository)

## Approach
- Cleaned and encoded categorical features using one-hot encoding
- Trained Logistic Regression and Random Forest classifiers
- Evaluated using Confusion Matrix, F1-Score, and ROC-AUC
- Used SHAP to explain individual predictions

## Results
- Random Forest achieved better performance (F1-Score: 0.49, AUC: 0.927) compared to Logistic Regression (F1-Score: 0.44, AUC: 0.903)
- Key influential features: duration, balance, poutcome
