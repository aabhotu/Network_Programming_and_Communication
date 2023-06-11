# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import socket
serverIP = "127.0.0.10"
serverPort = 10000
maxBytes = 4096

with open('content.txt', mode='rt', encoding='utf-8') as f:
  data = f.read()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(data.encode(), (serverIP, serverPort))
modifiedMessage, serverAddress = sock.recvfrom(maxBytes)
sock.close()

modifiedMessage = modifiedMessage.decode()
print(modifiedMessage)