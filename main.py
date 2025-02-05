from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import logging

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (specify frontend URL in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
try:
    model = joblib.load('fraud_detection_model.joblib')
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f" Error loading model: {e}")

# Serve static files (for HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define request model (including all 6 fields)
class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    Amount: float

# Define prediction endpoint
@app.post("/predict")
async def predict(transaction: Transaction):
    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([transaction.dict()])

        # Select only the 4 features the model expects
        input_data = input_data[['V1', 'V2', 'V3', 'V4']]

        # Ensure the input data has the correct shape
        if input_data.shape[1] != 4:
            raise HTTPException(status_code=400, detail="Input data must have exactly 4 features: V1, V2, V3, V4.")

        # Make prediction
        prediction = model.predict(input_data)

        # Return result
        result = "fraudulent" if prediction[0] == 1 else "legitimate"
        return {"prediction": result}
    except Exception as e:
        print(f" Error during prediction: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Serve the HTML file at the root URL "/"
@app.get("/")
async def serve_index():
    try:
        return FileResponse("static/form.html")  # Ensure this path is correct
    except Exception as e:
        print(f" Error serving index: {e}")
        raise HTTPException(status_code=500, detail="Error serving the HTML file.")
