 Fraud Detection API

Deployed Website Link: https://fraud-detection-3-77t1.onrender.com

 How To Run This Project

1. Clone the Repository:
sh git clone https://github.com/yenenesh12/fraud-detection.git
cd fraud-detection 

3. Install Dependencies:
sh pip install -r requirements.txt 

4. Prepare the Dataset:
Place your dataset (new.csv) in the project root directory. Ensure it contains:
- Time,V1, V2, V3, V4,Amount: Features for prediction.
- Class: 0 for legitimate, 1 for fraudulent.

4. Train the Model (Optional):
sh python train.py 

5. Run the Application:
sh python -m uvicorn main:app --reload 
Access the API at http://127.0.0.1:8000.


 File Structure
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


 API Endpoints

GET /: Serves the HTML form for testing.
POST /predict: Predicts whether a transaction is fraudulent or legitimate.


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

