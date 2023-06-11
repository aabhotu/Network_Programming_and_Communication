# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import socket

proxyIP = "127.0.0.10"
serverPort = 1000
maxBytes = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((proxyIP, serverPort))
sock.listen()
while True:
  connectionSocket, address = sock.accept()
  message = connectionSocket.recv(maxBytes)
  filename = message.decode().split()[1][1:]
  try:
    with open(filename, mode='rt', encoding='utf-8') as f:
      data = f.read()
      pass
    responseMessage = f"HTTP/1.1 200 OK\r\n\r\n{data}"
  except:
    print("Khong co du lieu tu may chu tam thoi")
    serverIP = "127.0.0.20"
    serverPort = 2000
    server_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_Sock.connect((serverIP, serverPort))

    request_message = f"""\
    GET /{filename} HTTP/1.1\r\n\
    Host: localhost\r\n\
    User-Agent: Group work 4\r\n\
    \r\n\
    """

    server_Sock.send(request_message.encode())
    RM_Temp = server_Sock.recv(maxBytes).decode()

    statusCode = RM_Temp.split()[1]
    ind = RM_Temp.find("\r\n\r\n") + 4
    data = RM_Temp[ind:]
    if statusCode=='200':
      with open(filename, mode='wt', encoding='utf-8') as f:
        f.write(data)
        print("Da luu du lieu tu may chu goc")
        pass
      responseMessage = f"HTTP/1.1 200 OK\r\n\r\n{data}"
    else:
      data = "<p>Khong tim thay du lieu tu may chu goc va tam thoi</p>"
      responseMessage = f"HTTP/1.1 404 Not Found\r\n\r\n{data}"
      pass
    pass
  connectionSocket.send(responseMessage.encode())
  connectionSocket.close()
  pass