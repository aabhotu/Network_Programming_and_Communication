import socket
import random

host = "localhost"
port = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))
while True:
  mess, add = sock.recvfrom(4096)
  print(add)
  mess = mess.decode()
  # print(mess)
  lenMess = str(len(mess))
  if random.random() >= 0.4:
    sock.sendto(lenMess.encode(), add)
  pass
