import pymongo
from pymongo import MongoClient

# def get_database():
 
#    # Provide the mongodb atlas url to connect python to mongodb using pymongo
#    CONNECTION_STRING = "mongodb+srv://bitcamp-2023:zfGBxA65Bku2aCPr@bitcamp-2023.0bp6oqs.mongodb.net/test"
 
#    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#    client = MongoClient(CONNECTION_STRING)
 
#    # Create the database for our example (we will use the same database throughout the tutorial
#    return client['stocks']
  
# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":   
  
#    # Get the database
#    dbname = get_database()

def insert_into_database(JSON_obj):

    connection_string = "mongodb+srv://bitcamp-2023:zfGBxA65Bku2aCPr@bitcamp-2023.0bp6oqs.mongodb.net/test"
    database_name = "<database>"

    # Create a MongoClient object
    client = pymongo.MongoClient(connection_string)

    # Get the database
    db = client[database_name]

    # create a database object
    mydb = client["mydatabase"]

    # create a collection object
    mycol = mydb["stocks"]

    # insert a document
    # mydict = { "name": "Snapchat", "Sentiment": 0.72 }
    mycol.insert_one(JSON_obj)

import pymongo

def get_data_from_mongodb():
    """
    Retrieves data from a MongoDB collection based on a query.

    Parameters:
        connection_string (str): The MongoDB connection string.
        database_name (str): The name of the MongoDB database.
        collection_name (str): The name of the MongoDB collection.
        query (dict): The query to retrieve data from the collection (optional).

    Returns:
        A list of documents that match the query.
    """
    # Create a MongoClient object
    connection_string = "mongodb+srv://bitcamp-2023:zfGBxA65Bku2aCPr@bitcamp-2023.0bp6oqs.mongodb.net/test"
    client = pymongo.MongoClient(connection_string)

    # Get the database
    db = client["mydatabase"]

    # Get the collection
    collection = db["stocks"]

    # Retrieve data from the collection based on the query
    data = collection.find()

    # Convert the data to a list of dictionaries
    # data_list = []
    # for document in data:
    #     data_list.append(document)

    return data


# print the inserted document ID
# print(x.inserted_id)
