#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp

def GetWifiPass():
    import subprocess
    networks, out = [], ''
    try:
        wifi = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('latin-1').split('\n')
        wifi = [i.split(":")[1][1:-1]
                for i in wifi if "All User Profile" in i]
        longestI = 1
        for i in wifi:
            if int(len(i)) > longestI:
                longestI = len(i)
        for name in wifi:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear'], shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('latin-1').split('\n')
                results = [b.split(":")[1][1:-1]
                            for b in results if "Key Content" in b]
                longestR = 1
                for i in results:
                    if int(len(i)) > longestR:
                        longestR = len(i)
            except subprocess.CalledProcessError:
                networks.append((name, ''))
                continue
            try:
                networks.append((name, results[0]))
            except IndexError:
                networks.append((name, ''))
    except subprocess.CalledProcessError:
        pass
    out += f'\033[1;36m  {"SSID":<{int(longestI + 1)}}\033[1;90m|\033[1;36m {"PASSWORD":<{int(longestR + 1)}}\n\033[1;90m'
    out += f'  {"-"*(longestI + 1)}|{"-"*(longestR + 6)}\n'
    for name, password in networks:
        out += f'\033[1;93m  {name:<{int(longestI + 1)}}\033[1;90m| \033[1;37m{password:<{int(longestR + 1)}}\n'
    print(out)
