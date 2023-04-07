import socket
from datetime import date
from datetime import datetime
from encryption import encryption
import os
print("El servidor se encuentra en ejecución...")
HOST = 'localhost'  # Dirección IP del servidor #25.72.66.152
PORT = 12345  # Puerto en el que escuchará el servidor

today = date.today()
now = datetime.now()

timeFormat = str(now.hour)+":"+str(now.minute)+":"+str(now.second)

logs_folder_path = "./logs"
logs_filename = "Logs_Server_" + \
    str(today)+"_"+str(now.hour)+str(now.minute)+str(now.second)+".txt"
if not os.path.exists(logs_folder_path):
    os.makedirs(logs_folder_path)
logs_file_path = os.path.join(logs_folder_path, logs_filename)
file = open(logs_file_path, "w")
logs = ""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST, PORT))
        s.listen()
        logs += timeFormat+" Info: Servidor esperando conexión.\n"
        print("Servidor esperando conexión...")

        conn, addr = s.accept()
        with conn:
            logs += timeFormat + \
                " Info: Conexión establecida con: "+str(addr)+"\n"
            print('Conexión establecida con:', addr)
            while True:
                logs += timeFormat+" Info: Mensaje recibido.\n"
                data = conn.recv(1024)
                if not data or encryption(data.decode(), "decrypt") == "Bye":
                    logs += timeFormat+" Info: Chat finalizado.\n"
                    break
                print(encryption(data.decode(), "decrypt"))
                respuesta = input("Ingrese respuesta: ")
                respuesta = encryption(respuesta, "encrypt")
                conn.sendall(respuesta.encode())
                logs += timeFormat+" Info: Mensaje enviado.\n"

    except Exception as e:
        logs += timeFormat+" Warning: Se ha perdido la conexión.\n"
logs += timeFormat + \
    " Info: El programa fue finalizado.  \n"
file.write(logs)
print("Programa finalizado.")