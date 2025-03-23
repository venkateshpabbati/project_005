from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import traceback

# Load the saved models
kmeans = joblib.load("kmeans_model.pkl")
pca = joblib.load("pca_model.pkl")
scaler = joblib.load("scaler.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Customer Segmentation API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json()
        df = pd.DataFrame(data)

        # Select relevant features (ensure same order as training)
        features = ["Income", "MntWines", "MntFruits", "MntMeatProducts", 
                    "MntFishProducts", "MntSweetProducts", "MntGoldProds", 
                    "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", 
                    "NumWebVisitsMonth"]
        df = df[features]
        
        # Scale the data
        df_scaled = scaler.transform(df)
        
        # Apply PCA
        df_pca = pca.transform(df_scaled)
        
        # Predict cluster
        clusters = kmeans.predict(df_pca)
        
        return jsonify({'clusters': clusters.tolist()})
    except Exception as e:
        app.logger.error(traceback.format_exc())
        return jsonify({'error': 'An internal error has occurred!'})

import os

# Run the app
if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(debug=debug_mode)