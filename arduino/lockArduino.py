import webcam, enviaimg, servidor 

webcam.tirar_foto_com_tecla('C:/Users/fernj/Pictures/capturaswebcam/foto.jpg')

metadata = {
    "tranca_id" : 1
}

enviaimg.enviar_imagem_para_servidor('C:/Users/fernj/Pictures/capturaswebcam/foto.jpg', metadata=metadata)


servidor.iniciarServidor()