#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp

def UPP():
    def OPT1():
        Olds = []; AddedUlt = []
        checkforplan = subprocess.check_output("powercfg /L", shell=True); checkforplan = str(checkforplan).split(" ")
        os.system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 >nul")
        newplans = subprocess.check_output("powercfg /L", shell=True); newplans = str(newplans).split(" ")
        for i in newplans: 
            if not i in checkforplan: AddedUlt.append(i)
        with open("misc/windows/PP/ultimate.txt", "w") as f: 
            for i in AddedUlt: f.write(str(i) + "\n")
        print("\n\033[1;92m Succesfuly added")
    def OPT2():
        with open("misc/windows/PP/ultimate.txt", "r") as f:
            RemThis = f.read()
        os.system(f"powercfg -delete {RemThis}")
        os.remove("misc/windows/PP/ultimate.txt")
        print("\n\033[1;92m Succesfuly removed")
    OPT1() if not os.path.exists("misc/windows/PP/ultimate.txt") else OPT2()

def BPP():
    def OPT1():
        Olds = []; AddedUlt = []
        checkforplan = subprocess.check_output("powercfg /L", shell=True); checkforplan = str(checkforplan).split(" ")
        os.system("powercfg -duplicatescheme 381b4222-f694-41f0-9685-ff5bb260df2e >nul")
        newplans = subprocess.check_output("powercfg /L", shell=True); newplans = str(newplans).split(" ")
        for i in newplans:
            if not i in checkforplan: AddedUlt.append(i)
        with open("misc/windows/PP/balanced.txt", "w") as f:
            for i in AddedUlt: f.write(str(i) + "\n")
        print("\n\033[1;92m Succesfuly added")
    def OPT2():
        with open("misc/windows/PP/balanced.txt", "r") as f:
            RemThis = f.read()
        os.system(f"powercfg -delete {RemThis}")
        os.remove("misc/windows/PP/balanced.txt")
        print("\n\033[1;92m Succesfuly removed")
    OPT1() if not os.path.exists("misc/windows/PP/balanced.txt") else OPT2()

def PPP():
    def OPT1():
        Olds = []; AddedUlt = []
        checkforplan = subprocess.check_output("powercfg /L", shell=True); checkforplan = str(checkforplan).split(" ")
        os.system("powercfg -duplicatescheme a1841308-3541-4fab-bc81-f71556f20b4a >nul")
        newplans = subprocess.check_output("powercfg /L", shell=True); newplans = str(newplans).split(" ")
        for i in newplans:
            if not i in checkforplan: AddedUlt.append(i)
        with open("misc/windows/PP/saver.txt", "w") as f:
            for i in AddedUlt: f.write(str(i) + "\n")
        print("\n\033[1;92m Succesfuly added")
    def OPT2():
        with open("misc/windows/PP/saver.txt", "r") as f:
            RemThis = f.read()
        os.system(f"powercfg -delete {RemThis}")
        os.remove("misc/windows/PP/saver.txt")
        print("\n\033[1;92m Succesfuly removed")
    OPT1() if not os.path.exists("misc/windows/PP/saver.txt") else OPT2()


def GWA():
    try:
        inf = str(subprocess.check_output("netsh wlan show wirelesscapabilities", shell=True)).split("\\")
        Not = []; Sup = []
        for i in inf:
            for a in i:
                if a == ":":
                    i = i[5::]
                    b = i.split(":")
                    c = str(b[0]).strip()
                    d = str(b[1]).strip()
                    if d.lower() == "supported": Sup.append(c)
                    elif d.lower() == "not supported": Not.append(c)
        print("  \n\033[1;92m Supported\033[1;93m Capabilities")
        for i in Sup: print(f"    \033[1;37m{i}")
        print("  \n\033[1;91m Unsupported\033[1;93m Capabilities")
        for i in Not: print(f"    \033[1;37m{i}")
    except: print("\n\033[1;91m No wireless adapter found...\033[0;37m")

def EnableGPEDIT():
    import os, sys
    try: open("./misc/windows/gpedit.bat", "x")
    except: pass
    gpedit = """
@echo off
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"  

if '%errorlevel%' NEQ '0' (  
    echo Requesting administrative privileges...  
    goto UACPrompt  
) else ( goto gotAdmin )  

:UACPrompt  
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"  
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    exit /B  

:gotAdmin  
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )   
    pushd "%CD%"  
    CD /D "%~dp0"  

@shift /0
pushd "%~dp0" 

dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum >gpedit.txt 
dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >>gpedit.txt 

for /f %%i in ('findstr /i . gpedit.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i" 
pause
    """
    with open("./misc/windows/gpedit.bat", "w+") as f:
        f.write(gpedit)

    os.system('start cmd /k "cd misc/windows/ && start gpedit.bat" && exit /b')
