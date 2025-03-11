import requests
import json
import os
import serial

def enviar_imagem_para_servidor(caminho_imagem, metadata):
    url = "http://192.168.1.111:8080/api/upload-image"  # URL do servidor Spring
    try:
        with open(caminho_imagem, "rb") as file:
            # Define o arquivo e os campos adicionais
            files = {"file": (os.path.basename(caminho_imagem), file, "image/jpeg")}
            data = {"metadata": json.dumps(metadata)}  # Converte o JSON para string

            # Envia a requisição com o arquivo e os dados adicionais
            response = requests.post(url, files=files, data=metadata)
            print("Resposta do servidor:", response.text)
            resposta = response.text
            if(resposta =='open'):
                enviar_comando_arduino('A')
                print("Tranca aberta!")
            elif (resposta == 'f'):
                enviar_comando_arduino('F')
                print("Tranca fechada.")
    except Exception as e:
        print(f"Erro ao enviar a imagem para o servidor: {e}")

    # Função para enviar comandos ao arduíno
def enviar_comando_arduino(comando: str):
    try:
        # Abre a conexão serial
        arduino = serial.Serial('COM3', 9600) # Configura a comunicação serial com o arduíno, COM3 sendo a porta onde ocorrerão as comunicações.
        arduino.write(comando.encode()) # Envia o comando
        arduino.close() # Fecha a conexão serial
        return True
        
    except Exception as e:
        print(f"Erro ao se comunicar com o arduíno: {e}")
        return False
