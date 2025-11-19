import os
import joblib
from app.config import CATEGORIZER_DIR  # Absolute import from config

# Paths to model and vectorizer
_MODEL_PATH = os.path.join(CATEGORIZER_DIR, "model.pkl")
_VECTORIZER_PATH = os.path.join(CATEGORIZER_DIR, "vectorizer.pkl")

_model = None
_vectorizer = None

def get_model_and_vectorizer():
    """
    Load ML model and vectorizer if they exist.
    Returns (model, vectorizer). None if missing.
    """
    global _model, _vectorizer

    if _model is None or _vectorizer is None:
        if not os.path.exists(_MODEL_PATH) or not os.path.exists(_VECTORIZER_PATH):
            print(f"⚠️ Model or vectorizer missing. Using fallback categorizer.")
            return None, None

        _model = joblib.load(_MODEL_PATH)
        _vectorizer = joblib.load(_VECTORIZER_PATH)

    return _model, _vectorizer

def categorize_transaction(text: str) -> str:
    """
    Categorize a transaction text using the loaded ML model.
    Falls back to a simple rule-based categorizer if files are missing.
    """
    model, vectorizer = get_model_and_vectorizer()

    if model is None or vectorizer is None:
        # Rule-based fallback
        text_lower = text.lower()
        if "bill" in text_lower or "electricity" in text_lower:
            return "Utilities"
        elif "payment" in text_lower or "transfer" in text_lower:
            return "Finance"
        elif "hello" in text_lower or "hi" in text_lower:
            return "Greeting"
        else:
            return "Other"

    # Convert text to numeric features
    X = vectorizer.transform([text])  # Must be 2D
    category = model.predict(X)[0]
    return category
