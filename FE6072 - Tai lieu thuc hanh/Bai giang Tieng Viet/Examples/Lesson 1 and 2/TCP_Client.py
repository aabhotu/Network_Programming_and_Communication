# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

from socket import *
serverIP = "127.0.0.11"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
message = "Number one"
print("Client send:", message)

clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(1024)
print("Client receive:", modifiedMessage.decode())
clientSocket.close()