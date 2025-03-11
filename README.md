# FaceLock - Tranca

## Descrição

Esse repositório compõe a parte da tranca do projeto FaceLock, que visa usar uma câmera para tirar fotos e abrir fechaduras eletrônicas. Possui 5 arquivos, incluindo o arquivo com o código para arduíno, que será usado como protótipo. 

## Requisitos

- Python 3.10;
- Arduino IDE;
- FastAPI;
- cv2;
- os;
- requests;
- json.

## Instalação

1. Passo 1: Clone este repositório:
   ```bash
   git clone https://github.com/jcfern87/SecurityLevel-Tranca
   ```
2. Passo 2: Instale as dependências:
   ```bash
   pip install "fastapi[standard]"
   ```

## Uso

Explique como executar o projeto com exemplos de comandos.

```bash
python lockArduino.py
```

## Estrutura do Projeto

```
/SecurityLevel-Tranca
│-- arduino
|   /trancaArduino
|   |   |-- trancaArduino.ino
|   |-- enviaimg.py
|   |-- servidor.py
|   |-- lockArduino.py
│   │-- webcam.py
│-- README.md
```

Cada arquivo tem uma função específica.&#x20;

- enviaimg.py

  Usa a biblioteca json para se conectar a um servidor e enviar imagens capturadas pela webcam para um servidor para serem editadas e processadas.
- servidor.py

  Usa a biblioteca do FastAPI para rodar um servidor que recebe requisições para se comunicar diretamente com a tranca, abrindo ou fechando ela.
- webcam.py

  Usa as bibliotecas vc2 e os para abrir a webcam e tirar uma foto para ser analisada.
- lockArduino.py

  Junta todas as funções por meio de imports e as usa na ordem: webcam, enviaimg e servidor.

## Contato

Para mais informações, entre em contato:

- Nome: Júlio César Alves Fernandes
- Email: fernjuliotrabalho432\@gmail.com
- LinkedIn: [https://github.com/jcfern87](https://github.com/jcfern87)

