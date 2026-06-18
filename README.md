# data-science-internship-phase2

# Task 1
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



# Task 2
# Customer Segmentation Using Unsupervised Learning

## Objective
Cluster mall customers based on spending habits using K-Means clustering, visualize clusters using PCA, and propose marketing strategies for each segment.

## Dataset
Mall Customers Dataset

## Approach
- Performed EDA on customer demographics and spending behavior
- Used Elbow Method to determine optimal number of clusters (K=5)
- Applied K-Means clustering on Income and Spending Score
- Used PCA to visualize clusters across Age, Income, and Spending Score
- Proposed targeted marketing strategies for each segment

## Results
- Identified 5 customer segments: Average Customers, High-Value Customers, Young Spenders, Conservative High Earners, and Low Engagement Customers
- PCA captured ~89% of variance using 2 components
