import requests

data = requests.get('http://127.0.0.1:8080/').json()

print(data)
