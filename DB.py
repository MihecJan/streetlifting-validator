import pymongo

def connectToDB():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['streetliftingValidatorDB']

    return db