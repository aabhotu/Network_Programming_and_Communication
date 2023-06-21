import socket
from datetime import datetime

serverIP ="127.0.0.1"
serverPort = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((serverIP, serverPort))
sock.listen()
while True:
  connection, add = sock.accept()
  mess = connection.recv(4096)
  try:
    file = open('HelloWord.html', 'r')
    data = file.read()
    file.close()
    connection.send("HTTP/1.1 200 OK\r\n\n".encode())
    connection.send(data.encode())
    msg = f"<p>Thoi diem: {datetime.now()} nhan duoc van ban co do dai: {len(data)} bytes </p>"
    connection.send(msg.encode())
    connection.close()
    print("Success")
  except:
    connection.send("HTTP/1.1 404 Not Found\r\n\n".encode())
    data = "<p>Ko tim thay file</p>"
    connection.send(data.encode())
    connection.close()
    pass
  pass