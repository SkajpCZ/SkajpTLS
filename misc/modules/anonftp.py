#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp

def FTPanonLOG():
    import ftplib
    def TryFTP(ip):
        print(f"\n\033[0;90m Wait a few seconds...")
        try:
            aftp = ftplib.FTP(ip)
            aftp.login("anonymous")
            print("\n\033[1;92m  SUCCESS \033[0;90m>\033[0m Logged with \033[1;93m[ anonymous ]\033[0m name")
            aftp.quit()
            return True
        except:
            print("\n\033[1;91m  FAILED \033[0;90m>\033[0m Unable to login in with \033[1;93m[ anonymous ]\033[0m name")
            return False

    ip = input(f"\n\033[1;93m FTP IP \033[0;90m> \033[0m")
    TryFTP(ip)
