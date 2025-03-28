import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from datetime import datetime
from db.mongo import get_collection

BASE_URL = "https://api.geckoterminal.com/api/v2"
COLLECTION = get_collection("tokens_dex")


def save_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def get_recent_pools(pages=5, network="solana"):
    all_pools = []
    for page in range(1, pages + 1):
        url = f"{BASE_URL}/networks/{network}/pools"
        params = {"limit": 20, "page": page}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            pools = response.json().get("data", [])
            all_pools.extend(pools)
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Erro ao buscar página {page}: {e}")
    return all_pools


def process_pools(pools):
    new_snapshots = 0

    for pool in pools:
        attr = pool.get("attributes", {})
        address = attr.get("address")
        if not address:
            continue

        name = attr.get("name", "N/A")
        snapshot = {
            "timestamp": datetime.utcnow().isoformat(),
            "price_usd": save_float(attr.get("base_token_price_usd")),
            "quote_token_price_usd": save_float(attr.get("quote_token_price_usd")),
            "volume_24h_usd": save_float(attr.get("volume_usd")),
            "liquidity_usd": save_float(attr.get("liquidity_usd")),
            "transactions_24h": int(attr.get("tx_count_h24") or 0)
        }

        existing = COLLECTION.find_one({"address": address})
        if existing:
            timestamps = {snap["timestamp"] for snap in existing.get("history", [])}
            if snapshot["timestamp"] not in timestamps:
                COLLECTION.update_one(
                    {"address": address},
                    {
                        "$push": {"history": snapshot},
                        "$set": {"last_updated": snapshot["timestamp"]}
                    }
                )
                new_snapshots += 1
        else:
            new_token = {
                "name": name,
                "address": address,
                "history": [snapshot],
                "first_seen": snapshot["timestamp"],
                "last_updated": snapshot["timestamp"]
            }
            COLLECTION.insert_one(new_token)
            new_snapshots += 1

    print(f"✅ {new_snapshots} snapshots salvos no Mongo Atlas.")


def main():
    print("📡 Coletando tokens recém-criados via GeckoTerminal...")
    pools = get_recent_pools()
    if not pools:
        print("⚠️ Nenhum pool encontrado.")
        return
    process_pools(pools)


if __name__ == "__main__":
    main()
