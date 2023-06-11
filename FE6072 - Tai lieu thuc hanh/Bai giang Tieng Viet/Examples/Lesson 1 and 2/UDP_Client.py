# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

from socket import *
serverIP = "127.0.0.10"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = "Number three"
print("Client send:", message)

clientSocket.sendto(message.encode(), (serverIP, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print("Client receive:", modifiedMessage.decode())
clientSocket.close()