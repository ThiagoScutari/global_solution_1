import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# ============================
# GERAR DADOS SIMULADOS
# ============================
def gerar_dados(qtd=500):
    dados = []
    for _ in range(qtd):
        r = random.random()
        if r < 0.25:  # Tempestade
            temp = round(random.uniform(25, 32), 1)
            umid = round(random.uniform(81, 100), 1)
            evento = 'tempestade'
        elif r < 0.50:  # Queimada
            temp = round(random.uniform(34, 42), 1)
            umid = round(random.uniform(10, 39), 1)
            evento = 'queimada'
        elif r < 0.75:  # Geada
            temp = round(random.uniform(-2, 4), 1)
            umid = round(random.uniform(70, 100), 1)
            evento = 'geada'
        else:  # Normal
            temp = round(random.uniform(15, 28), 1)
            umid = round(random.uniform(40, 70), 1)
            evento = 'normal'
        dados.append([temp, umid, evento])
    return pd.DataFrame(dados, columns=['temperatura', 'umidade', 'evento'])

# ============================
# TREINAR E SALVAR MODELO
# ============================
def treinar_modelo():
    df = gerar_dados()
    X = df[['temperatura', 'umidade']]
    y = df['evento']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    print("✅ Modelo treinado com sucesso!\n")
    print(classification_report(y_test, y_pred))

    # Salvar modelo
    caminho_saida = 'python_ml/models'
    os.makedirs(caminho_saida, exist_ok=True)
    joblib.dump(modelo, f'{caminho_saida}/modelo_evento.pkl')
    print(f"Modelo salvo em: {caminho_saida}/modelo_evento.pkl")

if __name__ == '__main__':
    treinar_modelo()