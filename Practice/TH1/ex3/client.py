import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
timeNow = str(time.time())
sock.sendto(timeNow.encode(), ("127.0.0.2", 10001))
mess, addServer  = sock.recvfrom(4096)
sock.close()
print("res: ", addServer)
print("len: ", mess.decode())
