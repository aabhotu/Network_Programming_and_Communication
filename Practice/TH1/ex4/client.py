import socket
from datetime import datetime
import time

host = "localhost"
port = 10000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
timeNow = str(datetime.now())
sock.sendto(timeNow.encode(), (host, port))
sock.settimeout(0.1)
delay = 2

time_sent = time.time()

try:
  data, add = sock.recvfrom(4096)
  time_rec = time.time()
  time_diff = time_rec - time_sent
  if time_diff < delay:
    print("mess: ", data.decode())
  else:
    print("error")
except socket.timeout():
  print("no response")

