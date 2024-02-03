import requests

response = requests.get(url="http://api.kanye.rest")

response.raise_for_status()

data = response.json()

print(data)