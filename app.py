from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import joblib
import os
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your frontend origin
origins = [
    "http://127.0.0.1:5000",  # Flask frontend (local)
    "http://localhost:5000",  # Another possible local address
    "https://health-predictor-tool.onrender.com",  # deployed frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows only specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Define model directory
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "random_forest_maternal_health.pkl")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")

# Define expected columns for retraining
EXPECTED_COLUMNS = ["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate", "RiskLevel"]

# Load model and scaler
try:
    if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
    else:
        raise FileNotFoundError(f"Model or Scaler not found in {MODEL_DIR}!")
except FileNotFoundError as e:
    raise HTTPException(status_code = 500, detail = str(e))
except Exception as e:
    raise HTTPException(status_code = 500, detail = f"Error loading the model or scaler: {str(e)}")

@app.get("/")
def home():
    return {"message": "Maternal Health Risk Predictor API is Running!"}

@app.post("/predict/")
def predict(Age: float, SystolicBP: float, DiastolicBP: float, BS: float, BodyTemp: float, HeartRate: float):
    try:
        # Make a prediction using input features
        
        # Create input feature array
        features = np.array([[Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate]])
        
        # Scale the input features
        features_scaled = scaler.transform(features)
        
        # Make a prediction
        prediction = model.predict(features_scaled)[0]
        
        # Map numerical prediction to risk level
        risk_mapping = {0: "low risk", 1: "mid risk", 2: "high risk"}
        
        return {"Predicted Risk Level": risk_mapping[prediction]}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = f"Error during prediction: {str(e)}")
