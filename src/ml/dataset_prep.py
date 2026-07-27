import pandas as pd

from sklearn.model_selection import train_test_split


class DatasetPreparator:

    def __init__(
        self,
        dataset_path="data/training/documents.csv"
    ):
        self.dataset_path = dataset_path

    def load_dataset(self):

        df = pd.read_csv(
            self.dataset_path
        )

        return df

    def prepare(self):

        df = self.load_dataset()

        X = df["text"]

        y = df["label"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.5,
            random_state=42,
            stratify=y
        )

        return (
            X_train,
            X_test,
            y_train,
            y_test
        )