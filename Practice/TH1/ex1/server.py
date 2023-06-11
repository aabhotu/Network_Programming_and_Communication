import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.2", 10000))
while True:
  mess, clientAdd = sock.recvfrom(4096)
  print(clientAdd)
  print("Thoi diem: ", datetime.now())
  print("Do dai: ", len(mess), "bytes")
  mess = mess.decode().upper()
  sock.sendto(mess.encode(), clientAdd)
  pass
