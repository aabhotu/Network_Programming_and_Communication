# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import socket
serverIP = "127.0.0.10"
serverPort = 10000
maxBytes = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((serverIP, serverPort))
while True:
  message, clientAddress = sock.recvfrom(maxBytes)
  print("Client address:", clientAddress)

  message = message.decode()
  modifiedMessage = message.upper()
  sock.sendto(modifiedMessage.encode(), clientAddress)
  pass