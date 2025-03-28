import requests
import json
import os
from datetime import datetime

def coletar_metricas_tokens():
    url = "https://api.dexscreener.com/latest/dex/pairs"

    response = requests.get(url)
    if response.status_code != 200:
        print("⚠️ Erro na API da DexScreener")
        return

    tokens = response.json().get("pairs", [])
    snapshot = {
        "collected_at": datetime.utcnow().isoformat(),
        "tokens": tokens
    }

    os.makedirs("data", exist_ok=True)
    with open("data/token_metrics.json", "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2)
    print("✅ Métricas dos tokens da DEX coletadas.")
