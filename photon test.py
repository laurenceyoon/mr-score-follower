import socket
import time
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen()

client_socket, addr = server_socket.accept()

print('Connected by', addr)

progress = 0

while True:
    msg = str(progress)
    client_socket.sendall(msg.encode())
    print('send 완료 ' + str(progress))
    progress += 1
    time.sleep(2)

client_socket.close()
server_socket.close()