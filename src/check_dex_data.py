# src/check_dex_data.py

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)

db = client["dexScannerDeploy"]
collection = db["tokens_dex"]

print("📊 Total de documentos:", collection.count_documents({}))
print("🔍 Exemplo de documento:")
print(collection.find_one())
