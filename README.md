# Customer Segmentation and Personality Analysis

## 📌 Project Overview
This project focuses on **customer segmentation** using **K-Means clustering** to analyze spending behavior and personality traits. The segmentation helps businesses **target the right customers** with personalized marketing strategies.

## 🔥 Features
- **Data Preprocessing**: Handling missing values, scaling, and dimensionality reduction.
- **Customer Clustering**: Using K-Means with PCA for efficient segmentation.
- **Flask API**: A RESTful API for customer segmentation predictions.
- **Streamlit UI**: An interactive web app for data visualization.
- **Cloud Deployment**: Ready for deployment on AWS, Render, or Hugging Face Spaces.

---

## 📂 Folder Structure
```
├── models/                 # Trained K-Means, PCA, and Scaler files
├── flask_app/              # Flask API for predictions
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Dependencies for Flask
├── streamlit_app/          # Streamlit UI for visualization
│   ├── app.py              # Streamlit application
│   ├── requirements.txt    # Dependencies for Streamlit
├── data/                   # Sample customer dataset
├── README.md               # Project documentation
```

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/customer-segmentation.git
cd customer-segmentation
```

### 2️⃣ Install Dependencies
For **Flask API**:
```bash
cd flask_app
pip install -r requirements.txt
python app.py
```

For **Streamlit App**:
```bash
cd streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

---

## 🖥️ API Usage
Once the Flask API is running, test it using **Postman** or cURL:
```bash
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d '{
    "Income": [60000, 35000],
    "MntWines": [500, 100],
    "MntFruits": [50, 20],
    "MntMeatProducts": [300, 50],
    "MntFishProducts": [100, 10],
    "MntSweetProducts": [50, 5],
    "MntGoldProds": [200, 20],
    "NumWebPurchases": [5, 2],
    "NumCatalogPurchases": [3, 1],
    "NumStorePurchases": [6, 3],
    "NumWebVisitsMonth": [4, 6]
}'
```

---

## 📊 Results & Insights
- **Cluster 0**: Budget-conscious customers with lower spending.
- **Cluster 1**: High-income customers who prefer premium products.

---

## ☁️ Deployment
### 🟢 Deploy to AWS (EC2)
1. Launch an **Ubuntu EC2 instance**.
2. Install dependencies: `pip install -r requirements.txt`
3. Start the app: `python app.py` or `streamlit run app.py`

### 🔵 Deploy to Render
1. Push the repository to GitHub.
2. Connect it to **Render**.
3. Deploy the Flask API & Streamlit UI as separate services.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 📩 Contact
For questions or contributions, feel free to reach out!

📧 Email: venkateshpabbati@gmail.com  
🐙 GitHub: [venkateshpabbati](https://github.com/venkateshpabbati)  
💼 LinkedIn: [venkateshpabbati](https://linkedin.com/in/venkateshpabbati)
