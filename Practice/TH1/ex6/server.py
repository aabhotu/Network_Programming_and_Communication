import socket
import time

host = '127.0.0.2'
port = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
print(f"Server ip: {host}  Port number: {port}")
sock.listen()
while True:
  connecttionSock, add = sock.accept()
  print(f"Client Ip: {add[0]}  Portnumber: {add[1]}")
  mess = connecttionSock.recv(4096)
  print("Thoi diem: ", time.time())
  filename = 'text.txt'
  with open(filename) as f:
    content = f.read()
  connecttionSock.send(content.encode())