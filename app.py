import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Superstore Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("superstore_cleaned.csv")
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

df = load_data()

st.title("📊 Global Superstore - Business Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

subcategory_filter = st.sidebar.multiselect(
    "Select Sub-Category",
    options=df[df['Category'].isin(category_filter)]['Sub-Category'].unique(),
    default=df[df['Category'].isin(category_filter)]['Sub-Category'].unique()
)

# Apply filters
filtered_df = df[
    (df['Region'].isin(region_filter)) &
    (df['Category'].isin(category_filter)) &
    (df['Sub-Category'].isin(subcategory_filter))
]

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")

with col2:
    st.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")

with col3:
    st.metric("Total Orders", filtered_df['Order ID'].nunique())

st.markdown("---")

# Charts row
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Category")
    category_sales = filtered_df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    category_sales.plot(kind='bar', ax=ax, color='steelblue')
    ax.set_ylabel("Sales ($)")
    st.pyplot(fig)

with col2:
    st.subheader("Sales by Region")
    region_sales = filtered_df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    region_sales.plot(kind='bar', ax=ax, color='darkorange')
    ax.set_ylabel("Sales ($)")
    plt.xticks(rotation=45)
    st.pyplot(fig)

st.markdown("---")

# Top 5 Customers by Sales
st.subheader("🏆 Top 5 Customers by Sales")
top_customers = (
    filtered_df.groupby('Customer Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
st.bar_chart(top_customers)

st.markdown("---")

# Raw data preview
with st.expander("View Filtered Data"):
    st.dataframe(filtered_df)
