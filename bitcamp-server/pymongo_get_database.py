import pymongo
from pymongo import MongoClient
import os

def insert_into_database(JSON_obj):
    connection_string = os.environ.get("MONGO_CONNECTION_STRING")

    # Create a MongoClient object
    client = pymongo.MongoClient(connection_string)

    # Get the database
    # db = client[database_name]

    # create a database object
    mydb = client["mydatabase"]

    # create a collection object
    mycol = mydb["stocks"]

    # insert a document
    # mydict = { "name": "Snapchat", "Sentiment": 0.72 }
    mycol.insert_one(JSON_obj)

import pymongo

def get_data_from_mongodb():
    # Create a MongoClient object
    connection_string = os.environ.get("MONGO_CONNECTION_STRING")
    client = pymongo.MongoClient(connection_string)

    # Get the database
    db = client["mydatabase"]

    # Get the collection
    collection = db["stocks"]

    # Retrieve data from the collection based on the query
    data = collection.find()

    return data



