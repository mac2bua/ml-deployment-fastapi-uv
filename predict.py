import pickle

from typing import Dict, Any, Literal, Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

class CustomerData(BaseModel):
    """
    Simplified Pydantic model for validating customer data inputs to ML model.
    """
    
    # Categorical fields with Literal types
    gender: Literal["male", "female"]
    seniorcitizen: Literal[0, 1]
    partner: Literal["yes", "no"]
    dependents: Literal["yes", "no"]
    phoneservice: Literal["yes", "no"]
    multiplelines: Literal["no", "yes", "no_phone_service"]
    internetservice: Literal["fiber_optic", "dsl", "no"]
    onlinesecurity: Literal["no", "yes", "no_internet_service"]
    onlinebackup: Literal["no", "yes", "no_internet_service"]
    deviceprotection: Literal["no", "yes", "no_internet_service"]
    techsupport: Literal["no", "yes", "no_internet_service"]
    streamingtv: Literal["no", "yes", "no_internet_service"]
    streamingmovies: Literal["no", "yes", "no_internet_service"]
    contract: Literal["month-to-month", "two_year", "one_year"]
    paperlessbilling: Literal["yes", "no"]
    paymentmethod: Literal["electronic_check", "mailed_check", "bank_transfer_(automatic)", "credit_card_(automatic)"]
    
    # Numerical fields with realistic bounds based on your statistics
    tenure: int = Field(ge=0, description="Customer tenure in months")
    monthlycharges: float = Field(ge=0.0, description="Monthly charges ($)")
    totalcharges: float = Field(ge=0.0, description="Total charges ($)")

class PredictResponse(BaseModel):
    churn_probability: float
    churn: bool



app = FastAPI(title='churn-prediction')

with open("model.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)

def predict_single(customer):
    churn = pipeline.predict_proba(customer)[0, 1]
    return float(churn)

@app.post("/predict")
def predict(customer: CustomerData) -> PredictResponse:
    try:
        churn = predict_single(customer.model_dump())
        return PredictResponse(
            churn_probability=churn,
            churn=churn >= 0.5
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Model prediction failed")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9696)