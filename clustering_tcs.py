import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
st.title("Clustering Dashboard")
data = pd.read_csv("C:/Users/Diya/clustered.csv")  # or generate it live

# Sidebar options
cluster_to_view = st.sidebar.selectbox("Select Cluster", sorted(data['Cluster'].unique()))

st.subheader(f"Distribution of Categorical Features for Cluster {cluster_to_view}")
filtered_data = data[data['Cluster'] == cluster_to_view]

# Plotting
for col in ['Sex', 'Housing', 'Saving accounts', 'Checking account', 'Purpose', 'Job']:
    fig, ax = plt.subplots()
    sns.countplot(x=col, data=filtered_data, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
st.subheader("Numerical Feature Distributions by Cluster")

numerical_features = ['Age', 'Credit amount', 'Duration']

for feature in numerical_features:
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x='Cluster', y=feature, data= data, palette='viridis', ax=ax)
    ax.set_title(f'{feature} Distribution by Cluster')
    ax.set_xlabel('Cluster')
    ax.set_ylabel(feature)
    st.pyplot(fig)

