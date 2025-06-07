# FIAP – Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="docs/fiap.jpeg" alt="FIAP - Faculdade de Informática e Administração Paulista" width="40%">
  </a>
</p>

---

# 🌦️ MVP de Monitoramento e Predição de Eventos Meteorológicos com ESP32 + Machine Learning

## 📌 Grupo: 46

## 👨‍🎓 Integrantes:
- Thiago Scutari – RM562831 | thiago.scutari@outlook.com  
- Henrique Ribeiro Siqueira – RM565044 | henrique.ribeiro1201@gmail.com  
- Mariana Cavalcante Oliveira – RM561678 | mari.kvalcant@gmail.com  

## 👩‍🏫 Professores:

### Tutor  
- Leonardo Ruiz Orabona  

### Coordenador  
- Andrei Godoi Chiovato  

---

## 📜 Descrição

Este projeto desenvolve um sistema inteligente de monitoramento ambiental com predição em tempo real de eventos climáticos como **queimadas, geadas e tempestades**, utilizando dados simulados de um sensor **DHT22** conectado a um **ESP32 simulado via Wokwi**. A lógica de predição é baseada em um modelo de **Machine Learning** treinado com **Scikit-Learn**, e os dados são analisados em tempo real através de comunicação serial **RFC2217**.

---

## 🧰 Tecnologias e Recursos

- **ESP32** simulado via Wokwi
- **Sensor DHT22** emulado
- **PlatformIO + VSCode** (firmware)
- **Python 3.10+**
- **pandas, scikit-learn, joblib**
- **matplotlib, streamlit**
- **RFC2217** para leitura remota da serial
- **Streamlit** para dashboard interativo

---

## 📁 Estrutura do Projeto

```plaintext
Global_Solutions/
├── ESP32_Firmware/               # Código embarcado do sensor DHT22 (PlatformIO)
│   ├── src/main.ino
│   └── platformio.ini
│
├── python_ml/
│   ├── src/
│   │   ├── read_serial.py                   # Captura e gravação de dados brutos
│   │   ├── treinar_modelo.py                # Geração do dataset e modelo
│   │   ├── prever_evento_metereologico.py   # Monitoramento + predição
│   │   ├── dashboard_terminal.py            # Gráficos em Matplotlib
│   │   └── dashboard.py                     # Interface interativa com Streamlit
│   ├── data/
│   │   └── previsoes_sensor_YYYYMMDD.csv    # Arquivo gerado com as predições
│   ├── models/
│   │   └── modelo_evento.pkl                # Modelo treinado
│   └── requirements.txt
│
├── docs/
│   └── README.md | estrutura + prints
├── video/
│   └── demonstracao.mp4
└── .gitignore / venv
```

---

## ▶️ Como Executar

### 🛠️ Requisitos:
```bash
pip install -r requirements.txt
```

### 🔹 1. Treinar o modelo

```bash
python python_ml/src/treinar_modelo.py
```

### 🔹 2. Simular ESP32 com Wokwi

- Configure `rfc2217ServerPort: 4000` no `diagram.json`
- Inicie a simulação

### 🔹 3. Rodar a predição

```bash
python python_ml/src/prever_evento_metereologico.py
```

---

## 📊 Visualização de Dados

### 📈 Dashboard com Matplotlib

```bash
python python_ml/src/dashboard_terminal.py
```

Exibe:
- Temperatura e umidade ao longo do tempo
- Gráfico de barras por tipo de evento

---

## 📋 Lógica de Classificação

| Evento      | Temperatura (°C) | Umidade (%) |
|-------------|------------------|-------------|
| Geada       | < 4              | > 70        |
| Queimada    | > 33             | < 40        |
| Tempestade  | 25 - 32          | > 80        |
| Normal      | outros casos     |             |

---

## 📽️ Demonstração

O vídeo de demonstração com sensor + predição em tempo real encontra-se na pasta `/video`.
Link youtube: https://youtu.be/lV0VRtBctgo
LInk Notion: https://sulfuric-print-a0d.notion.site/Global-Solution-205137e83ea580dc8c1dc0e57ae04021

---

## 📝 Licença

Creative Commons Attribution 4.0 International License  
[http://creativecommons.org/licenses/by/4.0](http://creativecommons.org/licenses/by/4.0)

---
