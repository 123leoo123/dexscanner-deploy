import requests
from datetime import datetime
import json
import os

def coletar_top500():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1
    }

    all_tokens = []
    for page in range(1, 3):  # 2 páginas = 500 tokens
        params["page"] = page
        response = requests.get(url, params=params)
        if response.status_code == 200:
            all_tokens.extend(response.json())

    snapshot = {
        "collected_at": datetime.utcnow().isoformat(),
        "tokens": all_tokens
    }

    os.makedirs("data", exist_ok=True)
    with open("data/top500_tokens_coingecko.json", "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2)
    print("✅ Coleta dos Top 500 tokens finalizada.")
