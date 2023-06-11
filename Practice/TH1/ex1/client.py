import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = "Lap trinh mang"
sock.sendto(data.encode(), ("127.0.0.2", 10000))
mess, addr = sock.recvfrom(4096)
print(addr)
sock.close()
mess = mess.decode()
print(mess)