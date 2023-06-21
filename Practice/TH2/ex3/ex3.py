import http.client
import json

conn = http.client.HTTPConnection("nominatim.openstreetmap.org")
add = "Bắc Từ Liêm"
url = f"/search?q={add}&format=json"
conn.request("GET", url)
response = conn.getresponse()
data = json.loads(response.read().decode())
conn.close()
result = data[0]
lon = result["lon"]
lat = result["lat"]
print(f"Kinh do: {lon} \nVi do: {lat}")

#! Error