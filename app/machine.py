import joblib
from sklearn.ensemble import RandomForestClassifier
from pandas import DataFrame
from datetime import datetime


class Machine:
    """
    A Class that creates and trains a Random Forest Classifier model for the "Random Monsters" pandas DataFrame.
    Provides methods to predict the target variable, to save and load the trained model,
    and to get information about the model.

    Parameters:
        - df (pandas DataFrame): The input DataFrame on which to train the Random Forest Classifier.
    """
    def __init__(self, df: DataFrame):
        """
        Initializes the Random Forest Classifier model by training it on the input pandas DataFrame.

        Parameters:
           - df (pandas DataFrame): The input DataFrame on which to train the Random Forest Classifier.
                        The DataFrame must contain a column named 'Rarity' which will be used as the target variable
                        for the classification model.

        Returns:
            - None
        """
        self.name = "Random Forest Classifier"
        self.timestamp = datetime.now()
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, feature_basis: DataFrame):
        """
        Takes a pandas DataFrame of input features and returns the predicted output variable and
            the confidence of the prediction.

        Parameters:
            - feature_basis (pandas DataFrame): The input DataFrame of features on which to make the prediction.

        Returns:
            - (prediction, confidence) (tuple): The predicted output variable and the confidence of the prediction.

        """
        confidence, *_ = self.model.predict_proba(feature_basis)
        prediction, *_ = self.model.predict(feature_basis)
        return prediction, max(confidence)

    def save(self, filepath):
        """
       Saves the trained model as a joblib file to the specified filepath.

        Parameters:
            - filepath (str): The path and filename for saving the trained model.

        Returns:
            - None
        """
        return joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        """
        Loads a joblib file from the specified filepath and returns the trained model.

        Parameters:
            - filepath (str): The path and filename for loading the trained model.

        Returns:
            - loaded (Machine object): The trained Machine object loaded from the specified filepath.
        """
        loaded = joblib.load(filepath)
        return loaded

    def info(self):
        """
        Returns a string with the name of the model and the timestamp of when the model was initialized.

        Parameters:
            - None

        Returns:
            - info (str): A string with the name of the model and the timestamp of when the model was initialized.
        """
        return f"{self.name} model initialized at {self.timestamp}"

