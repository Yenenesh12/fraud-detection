Fraud Detection API with FastAPI
This project implements a fraud detection system using a machine learning model trained on transaction data. The system is exposed as a REST API using FastAPI, allowing users to make predictions on whether a transaction is fraudulent or legitimate.

Features
FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.

RandomForestClassifier: A machine learning model used for classification tasks.

SMOTE: Synthetic Minority Over-sampling Technique to handle imbalanced datasets.

CORS Middleware: Allows cross-origin requests to the API.

Static File Serving: Serves static files (HTML, CSS, JS) for a simple frontend interface.

Prerequisites
Python 3.7+

Required Python packages: fastapi, uvicorn, pydantic, pandas, scikit-learn, imblearn, joblib

Installation
Clone the repository:

bash
Copy
git clone https://github.com/yourusername/fraud-detection-api.git
cd fraud-detection-api
Install dependencies:

bash
Copy
pip install -r requirements.txt
Run the FastAPI server:

bash
Copy
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000.

Usage
API Endpoints
GET /: Serves the HTML form for submitting transaction data.

POST /predict: Accepts transaction data and returns a prediction of whether the transaction is fraudulent or legitimate.

Example Request
To make a prediction, send a POST request to /predict with the following JSON body:

json
Copy
{
  "Time": 0.0,
  "V1": -1.359807,
  "V2": -0.072781,
  "V3": 2.536347,
  "V4": 1.378155,
  "Amount": 149.62
}
Example Response
json
Copy
{
  "prediction": "legitimate"
}
Frontend
The frontend is a simple HTML form that allows users to input transaction data and get predictions. It is served at the root URL /.

Model Training
The model is trained using a RandomForestClassifier on a dataset containing transaction data. The dataset is preprocessed by scaling the features and balancing the classes using SMOTE.

Steps to Train the Model
Load the dataset:

python
Copy
df = pd.read_csv("new.csv")
Select features and target:

python
Copy
X = df[['V1', 'V2', 'V3', 'V4']]
y = df['Class']
Normalize the features:

python
Copy
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
Split the data:

python
Copy
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)
Apply SMOTE:

python
Copy
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
Train the model:

python
Copy
model = RandomForestClassifier(n_estimators=10, max_depth=10, random_state=42, n_jobs=1)
model.fit(X_resampled, y_resampled)
Save the model:

python
Copy
joblib.dump(model, "fraud_detection_model.joblib")
Error Handling
400 Bad Request: If the input data does not have exactly 4 features (V1, V2, V3, V4).

500 Internal Server Error: If there is an error during prediction or serving the HTML file.

CORS Configuration
The API is configured to allow cross-origin requests from any origin (*). This can be restricted to specific origins in a production environment.

Running the Application
To run the application, use the following command:

bash
Copy
uvicorn main:app --reload
This will start the FastAPI server with hot-reloading enabled.

Conclusion
This project demonstrates how to build a simple fraud detection system using FastAPI and a machine learning model. The API can be easily extended or integrated into a larger system for real-time fraud detection.

License
This project is licensed under the MIT License. See the LICENSE file for details.
