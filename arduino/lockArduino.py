import webcam, enviaimg

webcam.tirar_foto_com_tecla('C:/Users/fernj/Pictures/capturaswebcam/foto.jpg')

metadata = {
    "metadata" : 1
}

enviaimg.enviar_imagem_para_servidor('C:/Users/fernj/Pictures/capturaswebcam/foto.jpg', metadata=metadata)


