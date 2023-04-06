import joblib
from sklearn.ensemble import RandomForestClassifier
from pandas import DataFrame
from datetime import datetime


class Machine:
    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        self.timestamp = datetime.now()
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, feature_basis: DataFrame):
        confidence, *_ = self.model.predict_proba(feature_basis)
        prediction, *_ = self.model.predict(feature_basis)
        return prediction, max(confidence)

    def save(self, filepath):
        return joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        loaded = joblib.load(filepath)
        return loaded

    def info(self):
        return f"{self.name} model initialized at {self.timestamp}"

