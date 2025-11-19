from fastapi import APIRouter
from ..services.prediction_services import predict_expense
from pydantic import BaseModel

router = APIRouter(prefix="/predict", tags=["prediction"])

class PredictIn(BaseModel):
    month: int
    year: int

@router.post("/")
def predict(payload: PredictIn):
    prediction = predict_expense(payload.month, payload.year)
    return {"predicted_expense": prediction}
