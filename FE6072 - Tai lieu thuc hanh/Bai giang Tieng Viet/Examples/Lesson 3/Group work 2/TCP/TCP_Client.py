# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import socket
serverIP = "127.0.0.10"
serverPort = 10000
maxBytes = 4096

with open('image.png', mode='rb') as f:
  data = f.read()
  pass

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((serverIP, serverPort))

sock.send(data)

sock.close()