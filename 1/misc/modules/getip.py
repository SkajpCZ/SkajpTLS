#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp
def myip():
    import requests, json, os, subprocess
    a = []
    try:public = requests.get("https://api.ipify.org/?format=json").json()['ip']
    except:public = "Failed to resolve"
    if os.name == 'nt':
        l=subprocess.check_output('ipconfig | findstr "v4"',shell=True)
        l=str(l).split("\\r")
        for i in l:
            i = i.split(":")
            for l in i:
                if'.'in l: 
                    if not'I'in l: a.append(l)
        a.reverse()
    else:
        if os.path.exists("/data/data/com.termux"):
            a.append("?")
        else:
            l = subprocess.check_output('ip a | grep inet', shell=True)
            l = str(l).split()
            for i in l:
                if '.' in i:
                    if not '127.0.0.1' in i:
                        if '/' in i:
                            a.append(i)
    print("\n\033[1;93m Public \033[1;90m> \033[1;37m" + public)
    print("\033[1;93m Private \033[1;90m> \033[1;37m" + a[0].strip())
