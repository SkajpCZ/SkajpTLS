
import socket, sys, threading, os, requests, json, time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# Choosing Nickname
def SetNickname():
    global nickname
    global mynick
    nickname = input("Choose your nickname: ")
    if len(nickname) < 1:
        SetNickname()
    mynick = nickname
SetNickname()

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("Server Disconnected")
            Connect()
            client.close()
            break


# Sending Messages To Server
def write():
    while True:
        message = '[1;93m' + nickname + '[0;37m: ' + input('')
        try:
            client.send(message.encode('ascii'))
        except UnicodeEncodeError:
            print("[1;91m Failed to send: Unkown character[1;37m")

# Starting Threads For Listening And Writing
def ConnectedToServer():
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def Connect():
    NotConnected = True
    while NotConnected:
        sys.stdout.write("]2;Connecting to server...")
        time.sleep(2)
        try:
            client.connect((str("127.0.0.1"), int(4444)))
            NotConnected = False
            sys.stdout.write("]2;Connected to 127.0.0.1")
            ConnectedToServer()
        except:
            Connect()
Connect()