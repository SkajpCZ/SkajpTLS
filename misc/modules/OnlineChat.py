#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp

def Server(lhost, lport, host, port):
    import socket
    import threading
    import os
    import random
    def Client(conip, conport):
        data = (f"""
import socket, sys, threading, os, requests, json, time

def clear():os.system('cls' if os.name == 'nt' else 'clear')
clear()

# Choosing Nickname
def SetNickname():
    global nickname
    global mynick
    nickname = input("Choose your nickname: ")
    if len(nickname) < 1:SetNickname()
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
        message = '\033[1;93m' + nickname + '\033[0;37m: ' + input('')
        try:
            client.send(message.encode('ascii'))
        except UnicodeEncodeError:
            print("\033[1;91m Failed to send: Unkown character\033[1;37m")

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
        sys.stdout.write("\x1b]2;Connecting to server...\x07")
        time.sleep(2)
        try:
            client.connect((str("{conip}"), int({conport})))
            NotConnected = False
            sys.stdout.write("\x1b]2;Connected to {conip}\x07")
            ConnectedToServer()
        except:Connect()
Connect()""")
        if os.path.exists(f"./misc/chats/{filename}.py"):
            with open(f"./misc/chats/{filename}.py", "w") as f:
                f.write(data)
                print(f"\033[1;90m Chat file created in './misc/chats/{filename}.py'")
        else:
            lolec = open(f"./misc/chats/{filename}.py", "x")
            with open(f"./misc/chats/{filename}.py", "w") as f:
                f.write(data)
                print(f"\033[1;90m Chat file created in './misc/chats/{filename}.py'")

    def clear():os.system('cls' if os.name == 'nt' else 'clear')
    clear()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((str(lhost), int(lport)))
    server.listen()

    clients = []
    nicknames = []

    def broadcast(message):
        for client in clients:
            client.send(message)

    def handle(client):
        while True:
            try:
                message = client.recv(1024)
                broadcast(message)
            except:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f"\033[1;91m - \033[1;37m{nickname}".encode('ascii'))
                print(f"\033[1;91m - \033[1;37m{nickname}")
                nicknames.remove(nickname)
                break

    def receive():
        while True:
            client, address = server.accept()
            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)
            print(f"\033[1;92m + \033[1;37m{nickname} \033[1;90mon\033[1;37m {str(address)}")
            broadcast(f"\033[1;92m + \033[0;37m{nickname}".encode('ascii'))
            client.send('\nConnected to server! Type something!\n'.encode('ascii'))
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

    print(f"Listening on {host} and port {port}...")
    filename = input("\n\033[1;93m Filename of client \033[1;90m> \033[1;37m")
    if len(filename) < 1:filename = f'client{random.randrange(0000,9999)}'
    Client(host, port)
    print("\n\n\033[1;90m To close server, close skajp tls and open it again")
    receive()


def Menu():
    print(f"\n\033[1;90m This will start server and create client to './misc/chats/'")

    lip = input("\n\033[1;93m Listening IP\033[1;90m > \033[1;37m")
    lport = input("\033[1;93m Listening PORT\033[1;90m > \033[1;37m")

    tip = input("\n\033[1;93m IP\033[1;90m > \033[1;37m")
    tport = input("\033[1;93m PORT\033[1;90m > \033[1;37m")
    Server(lip, lport, tip, tport)
