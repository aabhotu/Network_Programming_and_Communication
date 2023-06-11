import socket
import time

host = '127.0.0.2'
port = 10000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
print("Server ip: ", socket.gethostbyname(socket.gethostname()))
print("Client ip: ", sock.getpeername())
timeNow = str(time.time())
sock.send(timeNow.encode())
mess = sock.recv(4096)
print("mess: ", mess.decode())
sock.close()
