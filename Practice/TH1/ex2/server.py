import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.2", 10000))
sock.listen()
while True:
  connectionSocket, add = sock.accept()
  mess = connectionSocket.recv(4096)
  print("Thoi diem: ", datetime.now())
  print("Do dai: ", len(mess))
  mess = mess.decode().upper()
  connectionSocket.send(mess.encode())
  pass