from fastapi import FastAPI, HTTPException
import serial, uvicorn, os, signal

# Este código serve para criar e rodar um servidor local que se comunica diretamente com a porta utilizada pelo arduíno e recebe requests de um cliente através do FastAPI. Após receber um request, o código envia uma mensagem para o arduíno, que fechará ou abrirá. 

app = FastAPI() # Cria a aplicação FastAPI

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

def encerrarServidor():
    print("Encerrando o Servidor...")
    os.kill(os.getpid(), signal.SIGINT) # Envia um sinal para encerrar o servidor

# IP do servidor
host = "0.0.0.0"

# Rota para abrir a tranca
@app.post("/abrir")
async def abrir_tranca():
    if enviar_comando_arduino('A'): # Envia 'A' para abrir a tranca.
        encerrarServidor() # Encerra o servidor após a execução
        return {"status": "Tranca aberta."}
    else:
        raise HTTPException(status_code=500, detail="Erro ao abrir a tranca.")
# Rota para fechar a tranca
@app.post("/fechar")
async def fechar_tranca():
    if enviar_comando_arduino('F'): # Envia 'F' para fechar a tranca.
        encerrarServidor() # Encerra o servidor após a execução
        return {"status": "Tranca fechada."}
    else:
        raise HTTPException(status_code=500, detail="Erro ao fechar a tranca.")

# Rota para verificar o status do servidor
@app.get("/status")
async def status():
    return {"status": "Servidor rodando"}

# Inicia o servidor
def iniciarServidor():
    if __name__ == "__main__":
        uvicorn.run(app, host, port=8000)