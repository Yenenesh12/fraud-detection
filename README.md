<big>Fraud Detection API</big> 🚨
=====================================

<big>Overview</big> 📊
------------------------

This is a simple API for detecting fraudulent transactions. It uses a machine learning model to predict whether a transaction is legitimate or fraudulent based on several features.

<big>Deployed Website</big> 🌐
------------------------------

You can access the deployed website at: https://fraud-detection-3-77t1.onrender.com

<big>How to Run This Project</big> 💻
--------------------------------------

### Step 1: Clone the Repository 📁

git clone https://github.com/yenenesh12/fraud-detection.git
cd fraud-detection


### Step 2: Install Dependencies 📦

pip install -r requirements.txt


### Step 3: Prepare the Dataset 📊

Place your dataset (new.csv) in the project root directory. Ensure it contains:

* Time, V1, V2, V3, V4, Amount: Features for prediction
* Class: 0 for legitimate, 1 for fraudulent

### Step 4: Train the Model (Optional) 🤖

python train.py


### Step 5: Run the Application 🚀

python -m uvicorn main:app --reload


Access the API at http://127.0.0.1:8000.

<big>File Structure</big> 🗂️
------------------------------

* api: Main file (main.py)
* data: CSV file for the model
* model: Model file in joblib format
* notebooks: Data exploration files
* src: Train and predict files
* static: CSS files
* templates: HTML files
* .gitignore
* README.md
* requirements.txt

<big>API Endpoints</big> 📈
---------------------------

### GET / 📊

Serves the HTML form for testing.

### POST /predict 🤔

Predicts whether a transaction is fraudulent or legitimate.

Request Body:
{
  "Time": float,
  "V1": float,
  "V2": float,
  "V3": float,
  "V4": float,
  "Amount": float
}


Response:
{
  "prediction": "fraudulent" or "legitimate"
}
