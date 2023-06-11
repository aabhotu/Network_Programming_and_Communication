# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

from socket import *
serverIP = "127.0.0.10"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))
print("The server is ready to receive")
while True:
  message, clientAddress = serverSocket.recvfrom(2048)
  print("Server receive:", message.decode())

  capitalizedSentence = message.decode().upper()
  serverSocket.sendto(capitalizedSentence.encode(), clientAddress)