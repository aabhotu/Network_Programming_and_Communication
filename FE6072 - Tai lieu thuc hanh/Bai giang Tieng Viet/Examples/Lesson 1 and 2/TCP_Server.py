# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

from socket import *
serverIP = "127.0.0.11"
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
  connectionSocket, addr = serverSocket.accept()

  sentence = connectionSocket.recv(1024).decode()
  print("Server receive:", sentence)

  capitalizedSentence = sentence.upper()
  connectionSocket.send(capitalizedSentence.encode())
  connectionSocket.close()