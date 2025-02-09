Here's a refactored version of the README file with a more attractive format and a JSON example:

**Fraud Detection API**
==========================

**Overview**
------------

This is a simple API for detecting fraudulent transactions. It uses a machine learning model to predict whether a transaction is legitimate or fraudulent based on several features.

**Deployed Website**
--------------------

You can access the deployed website at: https://fraud-detection-3-77t1.onrender.com

**Getting Started**
-------------------

### Step 1: Clone the Repository

git clone https://github.com/yenenesh12/fraud-detection.git
cd fraud-detection


### Step 2: Install Dependencies

pip install -r requirements.txt


### Step 3: Prepare the Dataset

Place your dataset (new.csv) in the project root directory. Ensure it contains:

* Time, V1, V2, V3, V4, Amount: Features for prediction
* Class: 0 for legitimate, 1 for fraudulent

### Step 4: Train the Model (Optional)

python train.py


### Step 5: Run the Application

python -m uvicorn main:app --reload


Access the API at http://127.0.0.1:8000.

**File Structure**
------------------

.
api
main.py
data
new.csv
model
model.joblib
notebooks
data_exploration.ipynb
src
train.py
predict.py
static
style.css
templates
index.html
.gitignore
README.md
requirements.txt


**API Endpoints**
-----------------

### GET /

Serves the HTML form for testing.

### POST /predict

Predicts whether a transaction is fraudulent or legitimate.

**Request Body**

{
  "Time": 10.5,
  "V1": 0.5,
  "V2": 0.2,
  "V3": 0.1,
  "V4": 0.3,
  "Amount": 100.0
}


**Response**

{
  "prediction": "fraudulent" or "legitimate"
}


**Example Use Case**

You can use the API to predict whether a transaction is fraudulent or legitimate by sending a POST request to the /predict endpoint with the transaction data in the request body.

curl -X POST \
  http://127.0.0.1:8000/predict \
  -H 'Content-Type: application/json' \
  -d '{"Time": 10.5, "V1": 0.5, "V2": 0.2, "V3": 0.1, "V4": 0.3, "Amount": 100.0}'


This should return a response with the predicted outcome, either "fraudulent" or "legitimate".
