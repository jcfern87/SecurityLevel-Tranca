import cv2
import os

def tirar_foto_com_tecla(nome_arquivo, tecla='s'):
    # Exibe o diretório onde a foto será salva
    print(f"A foto será salva em: {os.path.abspath(nome_arquivo)}")

    # Inicializa a câmera (0 é a câmera padrão, pode variar dependendo do sistema)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro: Não foi possível abrir a câmera.")
        return

    print("Pressione a tecla 's' para tirar a foto ou 'q' para sair.")

    while True:
        # Captura um frame da câmera
        ret, frame = cap.read()

        if not ret:
            print("Erro: Não foi possível capturar a imagem.")
            break

        # Exibe o frame em uma janela
        cv2.imshow('Câmera', frame)

        # Aguarda 1 milissegundo e verifica se uma tecla foi pressionada
        key = cv2.waitKey(1) & 0xFF

        # Se a tecla 's' for pressionada, salva a foto
        if key == ord(tecla):
            cv2.imwrite(nome_arquivo, frame)
            print(f"Foto salva como {os.path.abspath(nome_arquivo)}")
            break

        # Se a tecla 'q' for pressionada, sai sem salvar
        if key == ord('q'):
            print("Captura cancelada.")
            break

    # Libera a câmera e fecha a janela
    cap.release()
    cv2.destroyAllWindows()
