import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.2", 10001))
print("server: ip: 127.0.0.2, PortNumber: 10001")
while True:
  mess, addClient = sock.recvfrom(4096)
  print("Thoi gian: ", datetime.now())
  print("Client: ", addClient)
  mess = mess.decode()
  lenMess = str(len(mess))
  sock.sendto(lenMess.encode(), addClient)
  pass