from pymongo import MongoClient

client = MongoClient("mongodb://mongo")
db = client['movies']