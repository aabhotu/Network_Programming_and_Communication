# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import socket
serverIP = "127.0.0.10"
serverPort = 1000
maxBytes = 4096

request_message = """\
GET /Helloworld.html HTTP/1.1\r\n\
Host: localhost\r\n\
User-Agent: Group work 3\r\n\
\r\n\
"""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((serverIP, serverPort))

sock.send(request_message.encode())
resposeMessage = sock.recv(maxBytes)
sock.close()

resposeMessage = resposeMessage.decode()
print(resposeMessage)