"""
Script: dashboard_terminal.py
Descrição: Gera gráficos usando matplotlib a partir de um arquivo CSV com previsões.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Caminho do arquivo mais recente
DATA_DIR = 'python_ml/data'
arquivos = sorted([f for f in os.listdir(DATA_DIR) if f.startswith("previsoes_sensor") and f.endswith(".csv")])
if not arquivos:
    print(" Nenhum arquivo de previsão encontrado em 'python_ml/data'")
    exit()

caminho_csv = os.path.join(DATA_DIR, arquivos[-1])
print(f" Usando dados de: {caminho_csv}")

# Ler os dados
df = pd.read_csv(caminho_csv)

# Converter timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Plot 1: Temperatura e umidade ao longo do tempo
plt.figure(figsize=(12, 5))
plt.plot(df['timestamp'], df['temperatura'], label='Temperatura (°C)', color='red')
plt.plot(df['timestamp'], df['umidade'], label='Umidade (%)', color='blue')
plt.legend()
plt.title("🌡️ Temperatura e 💧 Umidade ao longo do tempo")
plt.xlabel("Tempo")
plt.ylabel("Valor")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Contagem de eventos
plt.figure(figsize=(6, 4))
df['evento'].value_counts().plot(kind='bar', color='green')
plt.title(" Ocorrências por Evento Meteorológico")
plt.xlabel("Evento")
plt.ylabel("Frequência")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
