import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.2", 10000))
data = "Lap trinh mang"
sock.send(data.encode())
mess = sock.recv(4096)
sock.close()
mess = mess.decode()
print(mess)