"""
Descrição: Lê dados do sensor DHT22 via RFC2217 e usa um modelo de Machine Learning
           para prever eventos climáticos e gerar um CSV com os dados para visualização posterior.
"""

import pandas as pd
import joblib
import time
from datetime import datetime
import serial
import os

# Caminho do modelo
MODELO_PATH = 'python_ml/models/modelo_evento.pkl'
# Caminho de saída do CSV
CSV_DIR = 'python_ml/data'
os.makedirs(CSV_DIR, exist_ok=True)
CSV_PATH = os.path.join(CSV_DIR, f'previsoes_sensor_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')

# Armazena os dados durante a execução
historico = []

def prever_evento(temp, umidade):
    modelo = joblib.load(MODELO_PATH)
    entrada = pd.DataFrame([[temp, umidade]], columns=['temperatura', 'umidade'])
    predicao = modelo.predict(entrada)[0]
    probabilidade = modelo.predict_proba(entrada).max()
    return predicao, round(probabilidade, 2)

def monitorar_sensor():
    try:
        ser = serial.serial_for_url('rfc2217://localhost:4000', baudrate=115200, timeout=1)
        print("✅ Conectado ao sensor via RFC2217 (porta 4000)")
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
        return

    print("🔄 Aguardando dados do sensor...")
    print("-" * 50)

    try:
        while True:
            if ser.in_waiting > 0:
                linha = ser.readline().decode('utf-8').strip()
                if ',' in linha and not linha.startswith('id'):
                    try:
                        partes = linha.split(',')
                        temperatura = float(partes[-2])
                        umidade = float(partes[-1])
                        evento, confianca = prever_evento(temperatura, umidade)
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print(f"[{timestamp}] 🌡️ {temperatura}°C | 💧 {umidade}% --> 📊 {evento.upper()} (Confiança: {confianca})")

                        historico.append({
                            'timestamp': timestamp,
                            'temperatura': temperatura,
                            'umidade': umidade,
                            'evento': evento,
                            'confianca': confianca
                        })

                    except:
                        continue
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("\n🛑 Monitoramento encerrado pelo usuário.")
        # Salvar CSV ao final
        df = pd.DataFrame(historico)
        df.to_csv(CSV_PATH, index=False)
        print(f"📁 Dados salvos em: {CSV_PATH}")

if __name__ == '__main__':
    monitorar_sensor()
