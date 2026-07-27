import joblib


class DocumentClassifier:

    def __init__(self):

        self.model = joblib.load(
            "models/ml/classifier.pkl"
        )

        self.vectorizer = joblib.load(
            "models/ml/vectorizer.pkl"
        )

    def predict(
        self,
        text: str
    ):

        vector = self.vectorizer.transform(
            [text]
        )

        prediction = self.model.predict(
            vector
        )[0]

        probabilities = self.model.predict_proba(
            vector
        )[0]

        confidence = max(probabilities)

        return {
            "category": prediction,
            "confidence": round(
                float(confidence),
                4
            )
        }