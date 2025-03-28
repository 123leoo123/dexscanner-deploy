import sys
import os
import time

# Adiciona o diretório pai ao sys.path pra reconhecer o pacote 'coleta'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coleta import gecko, dex

print("🚀 Iniciando coleta contínua da DEX e CoinGecko...")

while True:
    try:
        print("🔄 Executando gecko.py...")
        gecko.main()

        print("🔄 Executando dex.py...")
        dex.main()

        print("⏳ Aguardando 10 minutos para próxima coleta...\n")
        time.sleep(600)

    except Exception as e:
        print(f"❌ Erro na execução: {e}")
        print("⏳ Tentando novamente em 5 minutos...\n")
        time.sleep(300)