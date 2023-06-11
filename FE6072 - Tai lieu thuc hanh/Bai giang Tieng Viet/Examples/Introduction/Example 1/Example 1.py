# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import socket, json, ssl
from urllib.parse import quote_plus

request_text = """\
GET /search?q={}&format=json HTTP/1.1\r\n\
Host: nominatim.openstreetmap.org\r\n\
User-Agent: Example 4\r\n\
Connection: close\r\n\
\r\n\
"""

def geocode(address):
  serverHostname = 'nominatim.openstreetmap.org'
  serverPort = 443
  unencrypted_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  unencrypted_sock.connect((serverHostname, serverPort))
  sock = ssl.wrap_socket(unencrypted_sock)
  request = request_text.format(quote_plus(address))

  print("Server socket address:", sock.getpeername())
  print("Client socket address:", sock.getsockname())

  sock.sendall(request.encode('ascii'))
  raw_reply = b''
  while True:
    more = sock.recv(4096)
    if not more:
      break
    raw_reply += more
  sock.close()
  rawreply_str = raw_reply.decode('utf-8')
  start = rawreply_str.find('[')
  for ind, s in enumerate(rawreply_str):
    if s == ']':
      end = ind
    pass
  reply = json.loads(rawreply_str[start:end + 1])
  return reply[0]['lat'], reply[0]['lon']

if __name__ == '__main__':
  address = 'Bac Tu Liem District'
  lat, lon = geocode(address)
  print(f"Coordinates of {address}:")
  print(f"Latitude: {lat}\nLongitude: {lon}")