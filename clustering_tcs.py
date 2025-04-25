import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Clustering Dashboard - All Clusters")
data = pd.read_csv("C:/Users/Diya/clustered.csv") 

st.write("First 5 rows of your data:")
st.write(data.head())

if 'Cluster' in data.columns:
    st.write("The 'Cluster' column exists.")
    st.write(f"Unique values in 'Cluster': {data['Cluster'].unique()}")
else:
    st.error("Error: The 'Cluster' column is missing in your CSV file.")
    st.stop()

categorical_cols = ['Sex', 'Housing', 'Saving accounts', 'Checking account', 'Purpose', 'Job']
numerical_features = ['Age', 'Credit amount', 'Duration']


st.header("Categorical Feature Distributions Across All Clusters")
for col in categorical_cols:
    st.subheader(f"Distribution of {col}")
    fig, ax = plt.subplots()
    sns.countplot(x=col, data=data, hue='Cluster', palette='viridis', ax=ax)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

st.header("Numerical Feature Distributions Across All Clusters")
for feature in numerical_features:
    st.subheader(f"Distribution of {feature}")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(y=feature, x='Cluster', data=data, palette='viridis', ax=ax)
    ax.set_title(f'{feature} Distribution Across All Clusters')
    ax.set_xlabel('Cluster')
    ax.set_ylabel(feature)
    st.pyplot(fig)

