# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import socket
serverIP = "127.0.0.10"
serverPort = 10000
maxBytes = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((serverIP, serverPort))
sock.listen()
while True:
  connectionSocket, address = sock.accept()
  message = connectionSocket.recv(maxBytes)
  print("TCP connection address:", address)

  message = message.decode()
  modifiedMessage = message.upper()
  connectionSocket.send(modifiedMessage.encode())
  pass