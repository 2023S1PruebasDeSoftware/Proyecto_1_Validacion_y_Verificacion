import socket
#
HOST = '25.72.66.152'  # Dirección IP del servidor
PORT = 12345  # Puerto en el que escucha el servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Escribe un mensaje: ')
        s.sendall(message.encode())
        data = s.recv(1024)
        print("hola")
        print('Respuesta del servidor:', data.decode())
