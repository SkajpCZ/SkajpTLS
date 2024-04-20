#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp

def main():
    import socket, time, threading, concurrent.futures
    open_ports = 0
    print_lock=threading.Lock()
    ips = input('\033[1;93m' + "\n Enter IPs \033[1;90m(split by \033[0;93m,\033[1;90m)" + '\033[1;90m' + " > " + '\033[0;37m' +f"")
    ports = int(input('\033[1;93m' + " Scan To Port \033[1;90m(\033[0;93m0\033[1;90m for all ports)" + '\033[1;90m' + " > " + '\033[0;37m' +f""))
    work = 100
    if ports == 0:
        ports = 65535
    if ports >= 32767:
        work = 200
    def scan(ip, port):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)
        try:
            scanner.connect((ip, port))
            scanner.close()
            with print_lock:
                print('\033[1;32m' + "\r Opened" + '\033[0;90m' + " > " + '\033[0;37m' + f"{port}    ")
        except:
            #print('\033[1;31m' + " Closed" + '\033[0;90m' + " > " + '\033[0;37m' + f"{port}", end="\r")
            pass
    if ',' in ips:
        for ip in ips.split(','):
            print('\033[1;93m' + "\n\n Scanning" + '\033[1;90m' + " > " + '\033[0;37m' +f"{ip}")
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
