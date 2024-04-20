#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp 

def MacAddrLookUp():
    import requests, json
    macaddr = input('\033[1;93m' + "\n MAC ADDRESS" + '\033[1;90m' + " > " + '\033[0;37m' +f"")
    apikey = "01gtrt4d83mhtwyxy75n4fb40z01gtrt5dmpsgscef9bkhtw0vqv4e7tu4hw2zxw"
    ipinf = f"https://api.maclookup.app/v2/macs/{macaddr}?apiKey={apikey}"
    stats = requests.get(ipinf)
    json_stats = stats.json()
    try:oui = json_stats["macPrefix"]; oui = oui[:2]+":"+oui[2:4]+":"+oui[4:];company = json_stats["company"];blockStart = json_stats["blockStart"];blockEnd = json_stats["blockEnd"];blockSize = json_stats["blockSize"];blockType = json_stats["blockType"];updated = json_stats["updated"];isRand = json_stats["isRand"];isPrivate = json_stats["isPrivate"]
    except:oui = "?";company = "?";blockStart = "?";blockEnd = "?";blockSize = "?";blockType = "?";updated = "?";isRand = "?";isPrivate = "?"

    print('\033[1;93m' + "\n OUI" + '\033[1;90m' + " > " + '\033[0;37m' +f"{oui}")
    print('\033[1;93m' + " Company" + '\033[1;90m' + " > " + '\033[0;37m' +f"{company}\n")

    print('\033[1;93m' + " Block Start" + '\033[1;90m' + " > " + '\033[0;37m' +f"{blockStart}")
    print('\033[1;93m' + " Block End" + '\033[1;90m' + " > " + '\033[0;37m' +f"{blockEnd}")
    print('\033[1;93m' + " Block Size" + '\033[1;90m' + " > " + '\033[0;37m' +f"{blockSize}")
    print('\033[1;93m' + " Block Type" + '\033[1;90m' + " > " + '\033[0;37m' +f"{blockType}\n")

    print('\033[1;93m' + " Updated" + '\033[1;90m' + " > " + '\033[0;37m' +f"{updated}")
    print('\033[1;93m' + " Rand" + '\033[1;90m' + " > " + '\033[0;37m' +f"{isRand}")
    print('\033[1;93m' + " Private" + '\033[1;90m' + " > " + '\033[0;37m' +f"{isPrivate}")
