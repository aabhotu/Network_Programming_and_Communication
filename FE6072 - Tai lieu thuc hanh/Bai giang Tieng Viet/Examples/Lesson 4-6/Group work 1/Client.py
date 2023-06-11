# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import socket
serverIP = "128.119.245.12"
serverPort = 80
maxBytes = 4096

request_message = """\
GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\n\
Host: gaia.cs.umass.edu\r\n\
User-Agent: Group work 1\r\n\
Connection: keep-alive\r\n\
Accept-Language: vn\r\n\
\r\n\
"""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((serverIP, serverPort))

sock.send(request_message.encode())
resposeMessage = sock.recv(maxBytes)
sock.close()

resposeMessage = resposeMessage.decode()
print(resposeMessage)
