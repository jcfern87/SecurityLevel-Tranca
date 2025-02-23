import requests
import json
import os

def enviar_imagem_para_servidor(caminho_imagem, metadata):
    url = "http://localhost:8080/api/upload-image"  # URL do servidor Spring
    try:
        with open(caminho_imagem, "rb") as file:
            # Define o arquivo e os campos adicionais
            files = {"file": (os.path.basename(caminho_imagem), file, "image/jpeg")}
            data = {"metadata": json.dumps(metadata)}  # Converte o JSON para string

            # Envia a requisição com o arquivo e os dados adicionais
            response = requests.post(url, files=files, data=data)
            print("Resposta do servidor:", response.text)
    except Exception as e:
        print(f"Erro ao enviar a imagem para o servidor: {e}")
