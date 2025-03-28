# src/db/mongo.py
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()  # <- Carrega o .env

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["dexScannerDeploy"]

def get_collection(name):
    return db[name]
