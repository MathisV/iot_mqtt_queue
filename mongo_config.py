from pymongo import MongoClient

# Configuration de la base de données MongoDB
MONGO_URI = '<CHANGE_ME>'
DATABASE_NAME = '<CHANGE_ME>'
COLLECTION_NAME = 'messages'

# Fonction de connexion à MongoDB
def connect_mongo():
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    return collection
