import pandas as pd
import joblib
import argparse
from statsmodels.tsa.arima.model import ARIMA
import os

# -----------------------------
# Argument parser (but paths fixed for your structure)
# -----------------------------
parser = argparse.ArgumentParser()
parser.add_argument(
    "--data",
    default="app/data/cleaned_sms.csv",   # Correct path in your backend folder
    help="Path to cleaned SMS CSV"
)
parser.add_argument(
    "--out",
    default="app/ml/predictor/model.pth",  
    help="Output model file"
)
args = parser.parse_args()

# -----------------------------
# Load dataset
# -----------------------------
if not os.path.exists(args.data):
    raise FileNotFoundError(f"❌ Data file not found: {args.data}")

df = pd.read_csv(args.data)

# Validate columns
required_cols = {"received_at", "amount"}
if not required_cols.issubset(df.columns):
    raise ValueError(f"CSV must contain columns: {required_cols}")

df["received_at"] = pd.to_datetime(df["received_at"], errors="coerce")
df = df.dropna(subset=["received_at", "amount"])

# -----------------------------
# Convert to monthly totals
# -----------------------------
df["month"] = df["received_at"].dt.to_period("M").dt.to_timestamp()
monthly = df.groupby("month")["amount"].sum().sort_index()

# -----------------------------
# ARIMA model training
# -----------------------------
print("Training ARIMA model... please wait...")
model = ARIMA(monthly, order=(2, 1, 2)).fit()

# -----------------------------
# Save model
# -----------------------------
os.makedirs(os.path.dirname(args.out), exist_ok=True)
joblib.dump(model, args.out)

print(f"✅ Predictor model saved to: {args.out}")
