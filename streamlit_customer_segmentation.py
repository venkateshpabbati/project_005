# Features of the Streamlit App
# ✅ Upload customer data (CSV)
# ✅ Preprocess and segment customers using K-Means
# ✅ Display cluster insights & visualizations

import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load saved models
kmeans = joblib.load("kmeans_model.pkl")
pca = joblib.load("pca_model.pkl")
scaler = joblib.load("scaler.pkl")

# Streamlit UI
def main():
    st.title("Customer Segmentation App")
    st.write("Upload customer data to get segmentation insights")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Select relevant features
        features = ["Income", "MntWines", "MntFruits", "MntMeatProducts", 
                    "MntFishProducts", "MntSweetProducts", "MntGoldProds", 
                    "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", 
                    "NumWebVisitsMonth"]
        df = df[features]
        
        # Scale and apply PCA
        df_scaled = scaler.transform(df)
        df_pca = pca.transform(df_scaled)
        
        # Predict clusters
        clusters = kmeans.predict(df_pca)
        df["Cluster"] = clusters
        
        st.write("### Clustered Data Sample")
        st.write(df.head())
        
        # Visualization
        st.write("### Cluster Distribution")
        fig, ax = plt.subplots()
        sns.countplot(x=df["Cluster"], palette="coolwarm", ax=ax)
        st.pyplot(fig)

if __name__ == "__main__":
    main()

# Next Steps
# 1. Run the Streamlit App:

# bash
# Copy code
# streamlit run streamlit_customer_segmentation.py
# 2. Upload a CSV file containing customer data.
# 3. View segmentation insights & visualizations.