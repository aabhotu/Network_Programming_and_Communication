import json
import socket
host = "nominatim.openstreetmap.org"
port = 80
add = "Quận Bắc Từ Liêm, Hà Nội"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
request = f"GET /search?q={add}&format=json HTTP1.1\r\nHost: {host}\r\n\r\n"
sock.send(request.encode())
response = b''
while True:
  data = sock.recv(4096)
  if not data:
    break
  response +=data
sock.close()
results = json.loads(response.decode())
for result in results:
  lat = result.get('lat')
  lon = result.get('lon')
  print(f"Kinh do: {lon} \nVi do: {lat}")