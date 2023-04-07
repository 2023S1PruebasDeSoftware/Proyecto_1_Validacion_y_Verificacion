import socket
#
HOST = 'localhost'  # Dirección IP del servidor #25.72.66.152
PORT = 12345  # Puerto en el que escucha el servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        while True:
            message = input('Escribe un mensaje: ')
            s.sendall(message.encode())
            data = s.recv(1024)
            if not data or data.decode() == "Bye":
                break
            print("hola")
            print('Respuesta del servidor:', data.decode())
    except Exception as e:
        print("Error al conectarse con el servidor.")