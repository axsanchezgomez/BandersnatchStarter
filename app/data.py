import doctest
from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """
    A class for interacting with a MongoDB database of monster data from the MonsterLab library.

    Attributes:
    - collection : str
                The MongoDB collection name you would like to use.
    >>> db = Database("Random Monsters")
    >>> db.reset()
    True
    >>> db.seed(1000)
    True
    >>> db.count()
    1000
    >>> df = db.dataframe()
    >>> isinstance(df, DataFrame)
    True
    >>> html = db.html_table()
    >>> "<table" in html
    True
    """
    load_dotenv()
    client = MongoClient(getenv("DB_URL"), tlsCAFile=where())["MonstersDB"]

    def __init__(self, collection: str):
        """
        Initializes the Database object with a specified MongoDB collection name.

        Parameters:
        - collection (str): The name of the MongoDB collection to use.
        """
        self.collection = self.client[collection]

    def seed(self, amount: int):
        """
        Seeds the database with a specified number of randomly generated monsters.

        Parameters:
        - amount (int): The number of monsters to generate and add to the database.
        """
        monster = [Monster().to_dict() for _ in range(amount)]
        return self.collection.insert_many(monster).acknowledged

    def reset(self):
        """
        Deletes all documents in the database.
        """
        return self.collection.delete_many({}).acknowledged

    def count(self) -> int:
        """
        Returns the number of documents in the database.

        Returns:
        - int: The number of documents in the database.
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """
        Returns a pandas DataFrame containing all documents in the database.

        Returns:
        - pandas.DataFrame: A DataFrame containing all documents in the database.
        """
        documents = self.collection.find({}, {"_id": 0})
        dataframe = DataFrame(documents)
        return dataframe

    def html_table(self) -> str:
        """
        Returns an HTML table containing all documents in the database.

        Returns:
        - str: An HTML table containing all documents in the database.
        """
        dataframe = self.dataframe()
        html = dataframe.to_html(index=False)
        return html

