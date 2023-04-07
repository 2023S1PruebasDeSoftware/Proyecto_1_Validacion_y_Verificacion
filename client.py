import socket
import re
from datetime import date
from datetime import datetime
from encryption import encryption
import os

today = date.today()
now = datetime.now()

timeFormat = str(now.hour)+":"+str(now.minute)+":"+str(now.second)

logs_folder_path = "./logs"
logs_filename = "Logs_Client_" + \
    str(today)+"_"+str(now.hour)+str(now.minute)+str(now.second)+".txt"
if not os.path.exists(logs_folder_path):
    os.makedirs(logs_folder_path)
logs_file_path = os.path.join(logs_folder_path, logs_filename)
file = open(logs_file_path, "w")

logs = ""

running = True
IpIsValid = False

while running and not IpIsValid:
    HOST = input("IP servidor: ")
    match = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", HOST)
    if (len(match) < 1 and HOST != "localhost"):
        logs += timeFormat+" Warning: Dirección IP ingresada no es válida\n"
        print("IP no valida")
    else:
        logs += timeFormat+" Info: Dirección IP ingresada es válida\n"
        IpIsValid = True
        PORT = 12345  # Puerto en el que escucha el servidor
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            logs += timeFormat+" Info: Intentado conectar con IP:" + \
                str(HOST)+" Puerto:12345"+"\n"
            for intento in range(1, 4):
                try:
                    logs += timeFormat + \
                        " Info: (Intento #" + str(intento) + \
                        ") Conectandose con el servidor..."+"\n"
                    print("(Intento #" + str(intento) +
                          ") Conectandose con el servidor...")
                    s.connect((HOST, PORT))
                    logs += timeFormat + \
                        " Info: Conexión establecida con éxito \n"
                    while True:
                        message = input('Escribe un mensaje: ')
                        message = encryption(message, "encrypt")
                        s.sendall(message.encode())
                        logs += timeFormat + \
                            " Info: Mensaje enviado \n"
                        data = s.recv(1024)
                        if not data or data.decode() == "Bye":
                            break
                        logs += timeFormat + \
                            " Info: Mensaje recibido \n"
                        print('Respuesta del servidor:', encryption(
                            data.decode(), "decrypt"))
                except Exception as e:
                    if intento < 3:
                        print("Error al conectarse con el servidor.")
                        logs += timeFormat + \
                            " Warning: Error al conectarse con el servidor. \n"
                    else:
                        print("No se pudo conectar con el servidor. ")
                        logs += timeFormat + \
                            " Warning: No se pudo conectar con el servidor.  \n"
logs += timeFormat + \
    " Info: El programa fue finalizado.  \n"
file.write(logs)
print("El programa fue finalizado")
