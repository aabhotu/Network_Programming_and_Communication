import socket
from datetime import datetime

host = '127.0.0.2'
port = 10000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host, port))
sock.listen()
print("client ip:", host )
while True:
  connectionSock, add = sock.accept()
  print("server ip: ", add[0])
  mess = connectionSock.recv(4096)
  print("Thoi diem: ", datetime.now())
  lenMess = str(len(mess.decode()))
  connectionSock.send(lenMess.encode())
  pass
