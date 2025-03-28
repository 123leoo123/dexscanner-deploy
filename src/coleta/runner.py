import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coleta import gecko, token_metrics

print("🚀 Iniciando coleta contínua da DEX e CoinGecko...")

while True:
    try:
        print("🔄 Executando gecko.py...")
        gecko.main()
        
        print("🔄 Executando token_metrics.py...")
        token_metrics.main()

        print("⏳ Aguardando 10 minutos para próxima coleta...\n")
        time.sleep(600)  # 10 minutos

    except Exception as e:
        print(f"❌ Erro na execução: {e}")
        print("⏳ Tentando novamente em 5 minutos...\n")
        time.sleep(300)  # Espera 5 minutos em caso de erro
