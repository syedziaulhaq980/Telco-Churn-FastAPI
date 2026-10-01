from fastapi import FastAPI
import joblib
from pathlib import Path
import pandas as pd
from pydantic import BaseModel


app = FastAPI(
    title="Telco Customer Churn Prediction API",
    description="API for predicting customer churn probability.",
    version="1.0.0"
)


# Path to trained model
MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "telco_churn_model.pkl"

# Load trained model
model = joblib.load(MODEL_PATH)
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def home():
    return {
        "message": "Telco Customer Churn Prediction API is running"
    }

@app.post("/predict")
def predict_churn(customer: CustomerData):
    input_data = customer.model_dump()

    input_df = pd.DataFrame([input_data])

    probability = model.predict_proba(input_df)[0][1]

    prediction = int(probability >= 0.30)

    return {
    "prediction": prediction,
    "prediction_label": "Churn" if prediction == 1 else "No Churn",
    "churn_probability": round(float(probability), 4),
    "threshold": 0.30
}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }