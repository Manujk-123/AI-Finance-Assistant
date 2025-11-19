from pydantic import BaseModel

class PredictionOut(BaseModel):
    predicted_next_month_total: float
