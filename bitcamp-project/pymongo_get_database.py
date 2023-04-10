import pymongo
from pymongo import MongoClient

def insert_into_database(JSON_obj):
    connection_string = "mongodb+srv://bitcamp-2023:zfGBxA65Bku2aCPr@bitcamp-2023.0bp6oqs.mongodb.net/test"

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
    data = []
    # Create a MongoClient object
    connection_string = "mongodb+srv://bitcamp-2023:zfGBxA65Bku2aCPr@bitcamp-2023.0bp6oqs.mongodb.net/test"
    client = pymongo.MongoClient(connection_string)

    # # Get the database
    db = client["mydatabase"]

    # # Get the collection
    collection = db["stocks"]
    print("collection: " + str(collection))

    # # Retrieve data from the collection based on the query
    # data = collection.find()

    return data



get_data_from_mongodb()