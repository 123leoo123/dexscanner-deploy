import time
from coleta import gecko, token_metrics

def run_loop():
    print("🔁 Iniciando coleta contínua...")
    while True:
        try:
            gecko.coletar_top500()
            token_metrics.coletar_metricas_tokens()
        except Exception as e:
            print(f"❌ Erro durante a coleta: {e}")
        time.sleep(300)  # 5 minutos entre coletas

if __name__ == "__main__":
    run_loop()
