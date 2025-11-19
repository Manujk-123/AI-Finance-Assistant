import os
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from app.ml.categorizer.preprocess import load_and_prep
from app.config import TRAINING_DATA_PATH, CATEGORIZER_DIR


def train_model():
    csv_path = TRAINING_DATA_PATH

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Training file not found: {csv_path}")

    df = pd.read_csv(csv_path)
    X, y = load_and_prep(df)

    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression(max_iter=200)
    model.fit(X_vec, y)

    os.makedirs(CATEGORIZER_DIR, exist_ok=True)
    joblib.dump(model, os.path.join(CATEGORIZER_DIR, "model.pkl"))
    joblib.dump(vectorizer, os.path.join(CATEGORIZER_DIR, "vectorizer.pkl"))

    print("Training completed successfully.")


if __name__ == "__main__":
    train_model()
