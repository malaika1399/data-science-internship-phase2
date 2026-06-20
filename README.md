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



### Task 5: Interactive Business Dashboard
Streamlit dashboard for Global Superstore sales/profit analysis with Region, Category, and Sub-Category filters.

## Objective
Develop an interactive Streamlit dashboard for analyzing sales, profit, and segment-wise performance using the Global Superstore dataset.

## Dataset
Global Superstore Dataset

## Approach
- Cleaned and prepared the dataset (handled missing values, converted date columns)
- Performed EDA on Sales, Profit, Category, and Region trends
- Built a Streamlit dashboard with interactive filters for Region, Category, and Sub-Category
- Displayed key KPIs: Total Sales, Total Profit, Total Orders
- Visualized Sales by Category and Sales by Region using bar charts
- Added a Top 5 Customers by Sales chart

## Results
- Total Sales: $1,710,971.47
- Total Profit: $288,920.44
- Total Orders: 867
- Technology category generates the highest sales among the three categories

## Live Dashboard:
         https://data-science-internship-phase2-ik5utc7wcarnrwmejkazeg.streamlit.app
