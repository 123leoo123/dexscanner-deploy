# src/db/mongo.py
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()  # <- Carrega o .env

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["dexScannerDeploy"]

def get_collection(name):
    return db[name]
