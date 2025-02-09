**Fraud Detection API**
==========================

**Deployed Website Link:** [Insert your deployed link here](#)

**Table of Contents**
-----------------

1. [How to Run This Project](#how-to-run-this-project)
2. [File Structure](#file-structure)
3. [API Endpoints](#api-endpoints)

**How to Run This Project**
---------------------------

### Step 1: Clone the Repository

git clone https://github.com/yenenesh12/fraud-detection.git
cd fraud-detection


### Step 2: Install Dependencies

pip install -r requirements.txt


### Step 3: Prepare the Dataset

Place your dataset (new.csv) in the project root directory. Ensure it contains:

* Time, V1, V2, V3, V4, Amount: Features for prediction.
* Class: 0 for legitimate, 1 for fraudulent.

### Step 4: Train the Model (Optional)

python train.py


### Step 5: Run the Application

python -m uvicorn main:app --reload


Access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

**File Structure**
-----------------

fraud-detection
├── api           # Main file (main.py)
├── data          # CSV file for the model
├── model         # Model file in joblib format
├── notebooks     # Data exploration files
├── src           # Train and predict files
├── static        # CSS files
├── templates     # HTML files
├── .gitignore    
├── README.md     
├── requirements.txt  


**API Endpoints**
-----------------

### GET /

Serves the HTML form for testing.

### POST /predict

Predicts whether a transaction is fraudulent or legitimate.

**Request Body**

{
  "Time": float,
  "V1": float,
  "V2": float,
  "V3": float,
  "V4": float,
  "Amount": float
}


**Response**

{
  "prediction": "fraudulent" or "legitimate"
}


**Example Use Case**

To use the API, send a POST request to [http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict) with the following JSON body:

{
  "Time": 10.0,
  "V1": 0.5,
  "V2": 0.2,
  "V3": 0.1,
  "V4": 0.3,
  "Amount": 100.0
}


The API will respond with a JSON object indicating whether the transaction is fraudulent or legitimate.
