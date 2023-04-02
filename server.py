import socket

HOST = '25.72.66.152'  # Dirección IP del servidor
PORT = 12345  # Puerto en el que escuchará el servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Conexión establecida con', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Recibido:",data)
            respuesta = input("Ingrese respuesta: ")
            conn.sendall(respuesta.encode())
