import os
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from src.ml.dataset_prep import DatasetPreparator


class DocumentClassifierTrainer:

    def __init__(self):

        self.dataset = DatasetPreparator()

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=5000
        )

        self.model = LogisticRegression(
            max_iter=1000,
            random_state=42
        )

    def train(self):

        X_train, X_test, y_train, y_test = (
            self.dataset.prepare()
        )

        X_train_vectors = self.vectorizer.fit_transform(
            X_train
        )

        self.model.fit(
            X_train_vectors,
            y_train
        )

        os.makedirs(
            "models/ml",
            exist_ok=True
        )

        joblib.dump(
            self.model,
            "models/ml/classifier.pkl"
        )

        joblib.dump(
            self.vectorizer,
            "models/ml/vectorizer.pkl"
        )

        print("Training completed successfully.")
        print("Model saved to models/ml/")