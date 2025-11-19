import pickle

class CategorizerModel:
    def __init__(self):
        self.model = None
        self.vectorizer = None

    def train(self, texts, labels):
        """
        Train a simple ML model (e.g. Logistic Regression)
        """
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression

        self.vectorizer = TfidfVectorizer()
        X = self.vectorizer.fit_transform(texts)

        self.model = LogisticRegression()
        self.model.fit(X, labels)

    def predict(self, text):
        if not self.model or not self.vectorizer:
            raise ValueError("Model not trained")
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]

    def save(self, model_path, vectorizer_path):
        with open(model_path, "wb") as f:
            pickle.dump(self.model, f)
        with open(vectorizer_path, "wb") as f:
            pickle.dump(self.vectorizer, f)

    def load(self, model_path, vectorizer_path):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)
        with open(vectorizer_path, "rb") as f:
            self.vectorizer = pickle.load(f)
