import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'experience':5, 'test':8, 'interview':10})

print(r.json())