import joblib

_model = None
_vectorizer = None


def get_classifier():
    global _model, _vectorizer

    if _model is None:
        _model = joblib.load("models/ml/classifier.pkl")

    if _vectorizer is None:
        _vectorizer = joblib.load("models/ml/vectorizer.pkl")

    return _model, _vectorizer


class DocumentClassifier:

    def __init__(self):
        self.model, self.vectorizer = get_classifier()

    def predict(self, text: str):

        vector = self.vectorizer.transform([text])

        prediction = self.model.predict(vector)[0]

        confidence = self.model.predict_proba(vector)[0].max()

        return {
            "category": prediction,
            "confidence": round(float(confidence), 4)
        }