import serial
import time

PORTA = 'COM6'
BAUD_RATE = 115200

try:
    with serial.Serial(PORTA, BAUD_RATE, timeout=1) as ser:
        print(f"Lendo dados da porta {PORTA}...")
        with open("dados_dht22.txt", "w") as arquivo:
            contador_vazio = 0
            while True:
                linha = ser.readline().decode('utf-8').strip()
                if linha:
                    contador_vazio = 0
                    print(linha)
                    arquivo.write(linha + '\n')
                else:
                    contador_vazio += 1
                    if contador_vazio > 10:  # aprox. 10 segundos sem dados
                        print("Nenhum dado recebido. Encerrando...")
                        break
                time.sleep(1)
except serial.SerialException as e:
    print(f"Erro ao abrir porta serial: {e}")
