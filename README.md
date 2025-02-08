Fraud Detection API
This is a FastAPI-based backend application that provides an API for detecting fraudulent transactions using a trained machine learning model. The project includes a web interface to interact with the API and a pre-trained Random Forest Classifier for fraud detection.

Table of Contents
Overview
Features
Prerequisites
Installation
Usage
API Endpoints
Model Training
Project Structure
Contributing
License
Overview
The goal of this project is to provide a simple, scalable, and efficient way to detect fraudulent transactions using machine learning. The backend API processes incoming transaction data, predicts whether it is fraudulent or legitimate, and returns the result. A static HTML form is provided for testing the API.

Features
Fraud Detection : Predicts whether a transaction is fraudulent or legitimate using a pre-trained Random Forest Classifier.
CORS Support : Allows cross-origin requests for seamless integration with frontend applications.
Static File Serving : Serves an HTML form for testing the API.
Error Handling : Provides meaningful error messages for invalid inputs or server errors.
Scalable Model : Trained on normalized and balanced data using SMOTE for better performance.
Prerequisites
Before running the application, ensure you have the following installed:

Python 3.8 or higher
pip (Python package manager)
uvicorn (ASGI server for running FastAPI)
Required Python libraries (see requirements.txt)

Installation
Step 1: Clone the Repository

git clone https://github.com/yenenesh12/fraud-detection.git
cd fraud-detection-api

Step 2: Install Dependencies
Install the required Python libraries using pip:

pip install -r requirements.txt

Step 3: Prepare the Dataset
Place your dataset (new.csv) in the root directory of the project. Ensure the dataset contains the following columns:

V1, V2, V3, V4: Features used for prediction.
Class: Target variable (0 for legitimate, 1 for fraudulent).

Step 4: Train the Model (Optional)
If you want to retrain the model, run the following command:
python train.py

This will generate a new fraud_detection_model.joblib file.

Usage
Running the Application
Start the FastAPI application using Uvicorn:

python -m uvicorn main:app --reload

The API will be available at http://127.0.0.1:8000.

Accessing the Web Interface
Open your browser and navigate to http://127.0.0.1:8000. You will see a form where you can input transaction details and get predictions.

API Endpoints
1. GET /
Description : Serves the static HTML form for testing the API.
Response : HTML file (form.html).
2. POST /predict
Description : Accepts transaction data and predicts whether it is fraudulent or legitimate.
Request Body :

json
{  
  "Time": float,  
  "V1": float,  
  "V2": float,  
  "V3": float,  
  "V4": float,  
  "Amount": float  
}

Response
json
{  
  "prediction": "fraudulent" or "legitimate"  
}

Model Training
The model is trained using the following steps:

Data Preprocessing :
Normalize features using StandardScaler.
Balance the dataset using SMOTE to handle class imbalance.

Model Selection :
Random Forest Classifier with hyperparameters:
n_estimators=10
max_depth=10
random_state=42
n_jobs=1

Saving the Model :
The trained model is saved as fraud_detection_model.joblib.
To retrain the model, update the dataset (new.csv) and run the training script:
bash
python train.py

Project Structure
1 fraud-detection-api/
2 ├── main.py                  # FastAPI application
3 ├── train_model.py           # Script for training the model
4 ├── fraud_detection_model.joblib  # Pre-trained model
5 ├── new.csv                  # Dataset used for training
6 ├── static/
7 │   └── form.html            # Static HTML form for testing the API
8 ├── requirements.txt          # List of dependencies
9 └── README.md                 # Project documentation

Contributing
Contributions are welcome! To contribute:

1.Fork the repository.
2.Create a new branch (git checkout -b feature/your-feature).
3.Commit your changes (git commit -m 'Add some feature').
4.Push to the branch (git push origin feature/your-feature).
5.Open a pull request.
License
This project is licensed under the MIT License
