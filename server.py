import socket
from datetime import date
from datetime import datetime
print("El servidor se encuentra en ejecución...")
HOST = 'localhost'  # Dirección IP del servidor #25.72.66.152
PORT = 12345  # Puerto en el que escuchará el servidor

today = date.today()
now = datetime.now()

timeFormat = str(now.hour)+":"+str(now.minute)+":"+str(now.second)

file = open("Logs_"+str(today)+".txt","w")
logs = ""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
    try:
        s.bind((HOST, PORT))
        s.listen()  
        logs += timeFormat+" Info: Servidor esperando conexión.\n"     
        print("Servidor esperando conexión...")
        
        conn, addr = s.accept()
        with conn:
            logs += timeFormat+" Info: Conexión establecida con: "+str(addr)+"\n"
            print('Conexión establecida con:', addr)
            while True:
                logs += timeFormat+" Info: Mensaje recibido.\n"
                data = conn.recv(1024)
                if not data or data.decode() == "Bye":
                    logs += timeFormat+" Info: Chat finalizado.\n"
                    break
                print(data.decode())
                respuesta = input("Ingrese respuesta: ")
                conn.sendall(respuesta.encode())
                logs += timeFormat+" Info: Mensaje enviado.\n"

    except Exception as e:
        logs += timeFormat+" Warning: Se ha perdido la conexión.\n"
file.write(logs)
print("Programa finalizado.")