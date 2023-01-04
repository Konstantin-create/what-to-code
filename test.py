import requests

responce = requests.post('https://e1-server.ml:1033', json={'prompt': 'code idea'})
print(responce.text)