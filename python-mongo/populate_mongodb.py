from pymongo import MongoClient
import pandas as pd
import json
import os

MONGO_URL = 'mongodb://localhost:27017'

cluster = MongoClient(MONGO_URL)

db = cluster['store']

for csv_file in os.listdir('./data'):
    # getting the path to csv
    path = os.path.join(os.getcwd(), 'data', csv_file)

    # reading data form csv
    df = pd.read_csv(path)

    # converting data to JSON format
    parsed_data = json.loads(df.to_json(orient='records'))

    # printing data
    print(json.dumps(parsed_data, indent=4))

    # getting collection name (collection name is the same as file name)
    collection_name = csv_file.split('.')[0]
    collection = db[collection_name]

    # emptying the collection
    collection.delete_many({})

    # writing data to mongodb collection.
    collection.insert_many(parsed_data)

    print('completed insterting:', collection_name, 'collection')


# closing the connection
cluster.close()
