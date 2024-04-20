#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp 

def ZipCracking():
    import zipfile, os, time, random
    global dpfile
    global folderCracked
    global count
    global finalDP

    count = 1
    def extrac(zfile, password):
        global count
        try:
            zfile.extractall(f"./misc/CrackedZips/{finalDP[0]}", pwd=bytes(password, 'utf-8'))
            return password
        except:
            spaceafter = " "*18
            print(f" \033[4;31mCracking\033[0;91m ({count}) \033[1;90m> \033[1;37m{password[:16]}{spaceafter*3}", end='\r')
            count += 1
            return

    def rockyou():
        global dpfile
        passlistlenght = len(open('./misc/wordlists/utf8-rockyou.txt', 'r', encoding='utf-8').readlines())
        passlistlenght = ('{:,}'.format(passlistlenght))
        zfile = zipfile.ZipFile(dpfile)
        passFile = open('./misc/wordlists/utf8-rockyou.txt', 'r', encoding='utf-8')
        print()

        for line in passFile.readlines():
            password = line.strip('\n')
            guess = extrac(zfile, password)
            if guess:
                spaceafter = " "*18
                print(f" \033[4;32mCracked\033[0;92m ({count}) \033[1;90m> \033[1;37m{password}{spaceafter*3}\n\n", end='\r')
                break

    def rand_digits():
        global dpfile
        zfile = zipfile.ZipFile(dpfile)
        print()
        for line in passFile.readlines():
            chars1 = "1234567890"
            password = ''.join((random.choice(chars1) for i in range(random.randint(2, 16))))
            guess = extrac(zfile, password)
            if guess:
                spaceafter = " "*18
                print(f" \033[4;32mCracked\033[0;92m ({count}) \033[1;90m> \033[1;37m{password}{spaceafter*3}\n\n", end='\r')
                break

    def every_rand():
        global dpfile
        zfile = zipfile.ZipFile(dpfile)
        passFile = open('./misc/wordlists/utf8-rockyou.txt', 'r', encoding='utf-8')
        print()
        for line in passFile.readlines():
            chars1 = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!._-*,"
            randsom = ''.join((random.choice(chars1) for i in range(random.randint(2, 16))))
            chars2 = "1234567890"
            num = ''.join((random.choice(chars2) for i in range(random.randint(2, 16))))
            rockpass = line.strip('\n')
            password = random.choice((randsom, rockpass, rockpass, rockpass, rockpass, rockpass, rockpass, randsom, randsom, num, num, randsom))
            guess = extrac(zfile, password)
            if guess:
                spaceafter = " "*18
                print(f" \033[4;32mCracked\033[0;92m ({count}) \033[1;90m> \033[1;37m{password}{spaceafter*3}\n\n", end='\r')
                break

    def CustomWordlists(passfile1):
        global dpfile
        passlistlenght = len(open(f'./misc/wordlists/{passfile1}', 'r', encoding='utf-8').readlines())
        passlistlenght = ('{:,}'.format(passlistlenght))
        zfile = zipfile.ZipFile(dpfile)
        passFile = open(f'./misc/wordlists/{passfile1}', 'r', encoding='utf-8')
        print()

        for line in passFile.readlines():
            password = line.strip('\n')
            guess = extrac(zfile, password)
            if guess:
                spaceafter = " "*18
                print(f" \033[4;32mCracked\033[0;92m ({count}) \033[1;90m> \033[1;37m{password}{spaceafter*3}\n\n", end='\r')
                break

    def MainMenu():
        
        cho = input("\033[1;93m Option \033[1;90m> \033[1;37m").lower()
        if cho == 'rockyou' or cho == '1':
            rockyou()
            MainMenu()
        if cho == 'digits' or cho == '2':
            rand_digits()
            MainMenu()
        if cho == 'random' or cho == '3':
            every_rand()
            MainMenu()
        if cho == 'custom' or cho == '4':
            ListsFound = ''
            for i in os.listdir("./misc/wordlists/"):
                ListsFound += f'{i},'
            print(f"\n\033[1;36m Wordlists: \033[1;37m{ListsFound}\n")
            passfile1 = input("\033[1;93m ./misc/wordlists/\033[1;37m")
            CustomWordlists(passfile1)
            MainMenu()
        if cho == 'exit' or cho == 'back':
            print()
        else:
            print("\n\033[1;91m Uknown options\n")
            MainMenu()

    FoundRockYou = True if os.path.exists("./misc/wordlists/utf8-rockyou.txt") else False
    if FoundRockYou == False:
        print('\033[1;32m' + "\n Downloading" + '\033[0;90m' + " > " + '\033[0;37m' + f"rockyou.txt  (modified to work with this script)  \n")
        if os.name == 'nt':
            os.system("curl -s https://raw.githubusercontent.com/SkajpCZ/Rockyou.txtUTF-8/main/utf8-rockyou.zip -o utf8-rockyou.zip && tar -xf utf8-rockyou.zip")
            os.system("del /F /S /Q utf8-rockyou.zip >nul")
            os.system("move utf8-rockyou.txt misc/wordlists/utf8-rockyou.txt >nul")
        else:
            os.system("curl -s https://raw.githubusercontent.com/SkajpCZ/Rockyou.txtUTF-8/main/utf8-rockyou.zip -o ./utf8-rockyou.zip && unzip ./utf8-rockyou.zip")
            os.system("rm ./utf8-rockyou.zip")
            os.system("mv utf8-rockyou.txt misc/wordlists/utf8-rockyou.txt")
    dpfile = input(f'\n\033[1;93m Drag your zip file here \033[1;90m> \033[1;37m')
    folderCracked = dpfile.strip('"').split('\\')
    folderCracked.reverse()
    folderCracked = folderCracked[0]
    dpfile = dpfile.replace('\\', '/').strip('"')
    dpfile = dpfile.strip("'").strip(" ")
    finalDP = dpfile.split("/")
    finalDP.reverse()
    print("\n\033[1;38;2;160;140;180m To go back type \033[4;38;2;190;180;200mback\033[0;37m\n")

    print("\n\033[1;36m Passwords Lists\033[1;90m:")
    print("\033[1;93m    1\033[1;90m)\033[1;37m Rockyou")
    print("\033[1;93m    2\033[1;90m)\033[1;37m Digits (Max 16 lenght)")
    print("\033[1;93m    3\033[1;90m)\033[1;37m Random (Mix of everything - 60% Rock you / 25% Random words / 15% Random digits)")
    print("\033[1;93m    4\033[1;90m)\033[1;37m Custom wordlist from './misc/wordlists'\n\n")
    MainMenu()
