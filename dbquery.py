def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    #CONNECTION_STRING = "mongodb+srv://localhost:27017/testAlgo"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient('localhost',27017)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['test_algo']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    collection_name = dbname["algo_details"]
    # item_1 = {
    # "item_name" : "Buble sort",
    # "difficulty" : "Easy",
    # "time_complexity": {
    #     "best": "n",
    #     "Average": "n2",
    #     "Worst": "n2"
    # },
    # "space_complexity" : "1",
    # "Stability" : "Yes",
    # }

    # item_2 = {
    # "item_name" : "Selection Sort",
    # "difficulty" : "Easy",
    # "time_complexity": {
    #     "best": "n2",
    #     "Average": "n2",
    #     "Worst": "n2"
    # },
    # "space_complexity" : "1",
    # "Stability" : "No",
    # }
    # collection_name.insert_many([item_1,item_2])
