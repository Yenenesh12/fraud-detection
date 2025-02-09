---

# 🚨 Fraud Detection API  

## 📊 Overview  
This is a simple API for detecting fraudulent transactions. It uses a machine learning model to predict whether a transaction is legitimate or fraudulent based on several features.  

---

## 🌐 Deployed Website  
🔗 Access the deployed website: [Fraud Detection API](https://fraud-detection-3-77t1.onrender.com)  

---

## 💻 How to Run This Project  

### 📁 Step 1: Clone the Repository  
git clone https://github.com/yenenesh12/fraud-detection.git
cd fraud-detection

### 📦 Step 2: Install Dependencies  
pip install -r requirements.txt

### 📊 Step 3: Prepare the Dataset  
Place your dataset (new.csv) in the project root directory. Ensure it contains:  

| Feature  | Description |
|----------|------------|
| Time   | Transaction time |
| V1, V2, V3, V4 | Anonymized transaction features |
| Amount | Transaction amount |
| Class  | 0 for legitimate, 1 for fraudulent |

### 🤖 Step 4: Train the Model *(Optional)*  
python train.py

### 🚀 Step 5: Run the Application  
python -m uvicorn main:app --reload
🔹 Access the API: [http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## 🗂 File Structure  
fraud-detection/
│── api/             # Main API file (main.py)
│── data/            # CSV dataset
│── model/           # Trained model file (.joblib)
│── notebooks/       # Data exploration notebooks
│── src/             # Training & prediction scripts
│── static/          # CSS files
│── templates/       # HTML files
│── .gitignore
│── README.md
│── requirements.txt

---

## 📈 API Endpoints  

### 📊 GET /  
Serves the HTML form for testing.  

### 🤔 POST /predict  
Predicts whether a transaction is fraudulent or legitimate.  

#### 📩 Request Body (JSON Format)  
{
  "Time": 12345.67,
  "V1": -1.23,
  "V2": 2.34,
  "V3": -0.56,
  "V4": 1.89,
  "Amount": 100.50
}

#### 📤 Response (JSON Format)  
{
  "prediction": "fraudulent" or "legitimate"
}

---

