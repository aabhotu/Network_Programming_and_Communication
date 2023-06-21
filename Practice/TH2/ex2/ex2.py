import requests
add = "Quận Bắc Từ Liêm, Hà Nội"
url = f"https://nominatim.openstreetmap.org/search?q={add}&format=json"
response = requests.get(url)
if(response.status_code==200):
  result = response.json()[0]
  longtitude = result["lon"]
  latitude = result["lat"]
  print(f"Kinh do: {longtitude} \nVi do: {latitude}")
else:
  print("Error")