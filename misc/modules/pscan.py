#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp

def main(ips = "none", ports = -1):
    import socket, time, threading, concurrent.futures
    open_ports = 0
    print_lock=threading.Lock()
    if ips == "none":ips = input('\033[1;93m' + "\n Enter IPs \033[1;90m(split by \033[0;93m,\033[1;90m)" + '\033[1;90m' + " > " + '\033[0m' +f"")
    if ports == -1:ports = int(input('\033[1;93m' + " Scan To Port \033[1;90m(\033[0;93m0\033[1;90m for all ports)" + '\033[1;90m' + " > " + '\033[0m' +f""))
    work = 100
    if ports==0:ports = 65535
    if ports>=32767:work = 200
    Valid = True

    try:
        for i in ips.split(","):
            for j in i.split("."):
                if len(j) == 4:
                    if j not in ["1","2","3","4","5","6","7","8","9","0"]:
                        Valid = False
                        break
            
    except:
        for j in ips.split("."):
            if len(j) == 4:
                if j not in ["1","2","3","4","5","6","7","8","9","0"]:
                    Valid = False
                    break



    def scan(ip, port):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)
        try:
            scanner.connect((ip, port))
            try: banner = scanner.recv(1024).decode();scanner.close()
            except:scanner.close()
            with print_lock:
                try: print(f"\033[1;32m\r Opened port\033[0;90m:\033[0m {f'{port}':<{6}} \033[0;90m|\033[1;93m Banner\033[0;90m: \033[0m{banner.rstrip()}")
                except: print(f"\033[1;32m\r Opened port\033[0;90m:\033[0m {f'{port}':<{6}}")
        except:pass
    
    if Valid:
        if ',' in ips:
            for ip in ips.split(','):
                print('\033[1;93m' + "\n\n Scanning" + '\033[1;90m' + " > " + '\033[0m' +f"{ip}")
                try:
                    with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:
                        for port in range(ports):
                            executor.submit(scan, ip, port)
                except KeyboardInterrupt:
                    print('\033[1;31m' + ' Stopping')
                    pass
        else:
            print("\n")
            try:
                with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:
                    for port in range(ports):
                        executor.submit(scan, ips, port)
            except KeyboardInterrupt:
                print('\033[1;31m' + ' Stopping')
                pass
        pass
    else:print(f"\n{bad} Invalid IP\033[0m")
