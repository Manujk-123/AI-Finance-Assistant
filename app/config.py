import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
CATEGORIZER_DIR = os.path.join(BASE_DIR, "ml", "categorizer")
PREDICTOR_DIR = os.path.join(BASE_DIR, "ml", "predictor")

TRAINING_DATA_PATH = os.path.join(DATA_DIR, "training_data.csv")
CLEAN_SMS_PATH = os.path.join(DATA_DIR, "clean_sms.csv")
DB_PATH = os.path.join(DATA_DIR, "transactions.db")
