try:
    from pymongo import MongoClient
    MONGO_AVAILABLE = True
except ImportError:
    MONGO_AVAILABLE = False


class MongoConnector:
    """
    A simple wrapper around PyMongo for storing and retrieving
    ML artifacts (model metadata, metrics, etc.) in MongoDB.
    """

    def __init__(self, uri: str, db_name: str):
        if not MONGO_AVAILABLE:
            raise ImportError("pymongo is not installed. Run: pip install pymongo")
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert(self, collection: str, document: dict):
        """Insert a single document (dictionary) into a collection."""
        return self.db[collection].insert_one(document)

    def find(self, collection: str, query: dict = None):
        """Retrieve documents from a collection matching the query."""
        if query is None:
            query = {}
        return list(self.db[collection].find(query))