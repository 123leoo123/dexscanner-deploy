# src/check_dex_data.py

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["dexScannerDeploy"]
collection = db["tokens_dex"]

print("📊 Total de documentos:", collection.count_documents({}))
print("🔍 Exemplo de documento:")
print(collection.find_one())
