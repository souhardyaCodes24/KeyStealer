import requests
import time

url = 'http://<ip-address>:5000/data'   # use your server’s IP, e.g. http://192.168.0.98:5000/data
payload = {'message': 'Hello from client'}

for i in range(10):
    response = requests.post(url, json=payload)
    print('Server responded:', response.text)
    time.sleep(5)
