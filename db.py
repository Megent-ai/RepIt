
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://RepIt:nwWlivobg74CSG37@cluster0.ykpjkfz.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

database = client['RepIt']
collection = database['RepIt']
def create(query):
    collection.insert_one(query)
def read(query):
    return