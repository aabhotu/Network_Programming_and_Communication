import socket
import time

host = '127.0.0.2'
port = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
timeNow = str(time.time())
sock.send(timeNow.encode())
mess = sock.recv(4096)
print("portnumber: ", sock.getsockname()[1])
print("mess: ", mess.decode())