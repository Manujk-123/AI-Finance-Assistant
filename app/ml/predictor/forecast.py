import joblib
import os
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pth")

def predict_next_month_from_series(series):
    # series is pandas Series indexed by month
    try:
        model = joblib.load(MODEL_PATH)
        forecast = model.forecast(steps=1)
        return float(forecast[0])
    except Exception as e:
        # fallback: simple average
        return float(series.mean())
