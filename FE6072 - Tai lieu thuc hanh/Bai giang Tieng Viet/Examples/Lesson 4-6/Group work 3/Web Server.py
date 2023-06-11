# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import socket

serverIP = "127.0.0.10"
serverPort = 1000
maxBytes = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((serverIP, serverPort))
sock.listen()
while True:
  connectionSocket, address = sock.accept()
  message = connectionSocket.recv(maxBytes)
  try:
    filename = message.decode().split()[1][1:]
    with open(filename, mode='rt', encoding='utf-8') as f:
      data = f.read()
      pass
    responseMessage = f"HTTP/1.1 200 OK\r\n\r\n{data}"
  except:
    data = "<p>Khong tim thay du lieu trong bo nho cua Server</p>"
    responseMessage = f"HTTP/1.1 404 Not Found\r\n\r\n{data}"
    pass
  connectionSocket.send(responseMessage.encode())
  connectionSocket.close()
  pass