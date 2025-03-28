import requests
import json
from datetime import datetime
import os

OUTPUT_PATH = "data/top_tokens_coingecko.json"

def main():
    print("📡 Coletando dados da CoinGecko...")

    all_tokens = []
    pages = [1, 2, 3, 4]  # 4 páginas de 250 = 1000 tokens (mas você pode parar em 800 se quiser)

    for page in pages:
        print(f"🔎 Página {page}...")
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 250,
            "page": page,
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            tokens = response.json()
            all_tokens.extend(tokens)

        except Exception as e:
            print(f"❌ Erro na página {page}: {e}")
            continue

    # Opcional: limitar para 800
    all_tokens = all_tokens[:800]

    data = {
        "collected_at": datetime.utcnow().isoformat(),
        "tokens": all_tokens
    }

    os.makedirs("data", exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("✅ Dados da CoinGecko coletados e salvos!")

if __name__ == "__main__":
    main()
