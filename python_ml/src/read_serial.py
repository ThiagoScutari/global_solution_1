import serial
import time
from datetime import datetime

def capturar_dados_sensor():
    """
    Captura dados do ESP32 simulado via porta RFC2217
    e salva automaticamente em arquivo .txt
    """
    
    # Conectar à porta serial virtual do Wokwi
    print("Conectando ao ESP32 simulado...")
    try:
        ser = serial.serial_for_url('rfc2217://localhost:4000', baudrate=115200, timeout=1)
        print("✅ Conectado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
        print("Certifique-se de que a simulação Wokwi está rodando com rfc2217ServerPort = 4000")
        return
    
    # Nome do arquivo com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"dados_sensor_{timestamp}.txt"
    
    print(f"📁 Salvando dados em: {nome_arquivo}")
    print("🔄 Capturando dados... (Ctrl+C para parar)")
    print("-" * 50)
    
    contador = 0
    
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        try:
            while True:
                if ser.in_waiting > 0:
                    linha = ser.readline().decode('utf-8').strip()
                    
                    if linha:
                        print(linha)  # Mostrar no terminal
                        arquivo.write(linha + '\n')  # Salvar no arquivo
                        arquivo.flush()  # Garantir que é salvo imediatamente
                        contador += 1
                
                time.sleep(0.1)  # Pequena pausa
                
        except KeyboardInterrupt:
            print(f"\n🛑 Captura interrompida pelo usuário")
            print(f"📊 Total de linhas capturadas: {contador}")
            print(f"💾 Dados salvos em: {nome_arquivo}")
    
    ser.close()

def enviar_comando(comando):
    """
    Envia comandos para o ESP32 (EXPORT, STATUS, CLEAR)
    """
    try:
        ser = serial.serial_for_url('rfc2217://localhost:4000', baudrate=115200, timeout=1)
        print(f"📤 Enviando comando: {comando}")
        ser.write(f"{comando}\n".encode())
        
        # Aguardar resposta
        time.sleep(2)
        while ser.in_waiting > 0:
            linha = ser.readline().decode('utf-8').strip()
            print(linha)
        
        ser.close()
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        comando = sys.argv[1].upper()
        if comando in ['EXPORT', 'STATUS', 'CLEAR']:
            enviar_comando(comando)
        else:
            print("Comandos válidos: EXPORT, STATUS, CLEAR")
    else:
        capturar_dados_sensor()