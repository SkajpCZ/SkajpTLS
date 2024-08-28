#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp
def main():
    import subprocess
    ## Colors
    grey = "\033[0;90m"
    red = "\033[0;31m"
    white = "\033[0m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"

    # Statuses
    bad = "\033[0;90m[\033[0;31m-\033[0;90m]\033[0m"
    good = "\033[0;90m[\033[0;32m+\033[0;90m]\033[0m"
    status = "\033[0;90m[\033[0;33m~\033[0;90m]\033[0m"


    interf = input(f"\n{status} \033[1;93mInterface{grey}:{white} ")
    down = False

    try:subprocess.run(['sudo', 'ip', 'link', 'set', 'down', interf],check=True);print(f"{good} Adapter {yellow}{interf}{white} is down");down=True
    except subprocess.CalledProcessError as e:print(f"{bad} Can't set down adapter {yellow}{interf}{white}: {red}{e}{white}")
    if down:
        try:subprocess.run(['sudo', 'macchanger', '-A', interf],check=True);print(f"{good} Changed mac on adapter {yellow}{interf}{white}");down=True
        except subprocess.CalledProcessError as e:print(f"{bad} Can't change mac on adapter {yellow}{interf}{white}: {red}{e}{white}")
        try:subprocess.run(['sudo', 'ip', 'link', 'set', 'up', interf],check=True);print(f"{good} Adapter {yellow}{interf}{white} is up");down=True
        except subprocess.CalledProcessError as e:print(f"{bad} Can't set up adapter {yellow}{interf}{white}: {red}{e}{white}")

def reset():
    import subprocess
    ## Colors
    grey = "\033[0;90m"
    red = "\033[0;31m"
    white = "\033[0m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"

    # Statuses
    bad = "\033[0;90m[\033[0;31m-\033[0;90m]\033[0m"
    good = "\033[0;90m[\033[0;32m+\033[0;90m]\033[0m"
    status = "\033[0;90m[\033[0;33m~\033[0;90m]\033[0m"


    interf = input(f"\n{status} \033[1;93mInterface{grey}:{white} ")
    down = False

    try:subprocess.run(['sudo', 'ip', 'link', 'set', 'down', interf],check=True);print(f"{good} Adapter {yellow}{interf}{white} is down");down=True
    except subprocess.CalledProcessError as e:print(f"{bad} Can't set down adapter {yellow}{interf}{white}: {red}{e}{white}")
    if down:
        try:subprocess.run(['sudo', 'macchanger', '-p', interf],check=True);print(f"{good} Mac reset on adapter {yellow}{interf}{white}");down=True
        except subprocess.CalledProcessError as e:print(f"{bad} Can't reset mac on adapter {yellow}{interf}{white}: {red}{e}{white}")
        try:subprocess.run(['sudo', 'ip', 'link', 'set', 'up', interf],check=True);print(f"{good} Adapter {yellow}{interf}{white} is up");down=True
        except subprocess.CalledProcessError as e:print(f"{bad} Can't set up adapter {yellow}{interf}{white}: {red}{e}{white}")
