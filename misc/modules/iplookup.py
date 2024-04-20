#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp

def IPLookUp():
    import requests, json
    InfoFromIPAPI_CO = False
    bad = "\033[0;90m[\033[0;31m-\033[0;90m]\033[0m"
    good = "\033[0;90m[\033[0;32m+\033[0;90m]\033[0m"
    status = "\033[0;90m[\033[0;33m~\033[0;90m]\033[0m"
    def NULLvals(): Cont = "?"; ContC = "?"; Country = "?"; CountryC = "?"; Reg = "?"; RegN = "?"; City = "?"; Dist = "?"; ZIP = "?"; Lat = "?"; Lon = "?"; Time = "?"; Cur = "?"; ISP = "?"; ORG = "?"; As = "?"; Asname = "?"; rever = "?"; mob = "?"; proxy = "?"; hosting = "?"
    ip = input('\033[1;93m' + "\n Enter IP" + '\033[1;90m' + " > " + '\033[0;37m' +f"")
    url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting"
    r = requests.get(url)
    rj = r.json()
    Status = rj["status"]
    if Status == "success":
        try:
            Cont = rj["continent"];ContC = rj["continentCode"];Country = rj["country"];CountryC = rj["countryCode"];Reg = rj["region"];RegN = rj["regionName"];City = rj["city"];Dist = rj["district"];ZIP = rj["zip"];Lat = rj["lat"];Lon = rj["lon"];Time = rj["timezone"];Cur = rj["currency"];ISP = rj["isp"];ORG = rj["org"];As = rj["as"];Asname = rj["asname"];rever = rj["reverse"];mob = rj["mobile"];proxy = rj["proxy"];hosting = rj["hosting"]
            try: rj1 = requests.get(f"http://ipapi.co/{ip}/json/").json(); net = rj1["network"]; lang = rj1["languages"]; tld = rj1["country_tld"]; InfoFromIPAPI_CO = True
            except: InfoFromIPAPI_CO = False; NULLvals(); pass
        except Exception as e: print(f"\n\033[1;91m Error: {e}\033[0;37m")
        # Print output
        if InfoFromIPAPI_CO:
            print(f"\n\033[1;93m Network \033[1;90m: \033[0;37m {net}")
            print('\033[1;93m' + " City" + '\033[1;90m' + ": " + '\033[0;37m' +f"{City}")
            print('\033[1;93m' + " Languages" + '\033[1;90m' + ": " + '\033[0;37m' +f"{lang}")
            print('\033[1;93m' + " Region" + '\033[1;90m' + " > " + '\033[0;37m' +f"{Reg}")
            print('\033[1;93m' + " Region Name" + '\033[1;90m' + " > " + '\033[0;37m' +f"{RegN}")
            print('\033[1;93m' + " Country" + '\033[1;90m' + " > " + '\033[0;37m' +f"{Country}")
            print('\033[1;93m' + " Country Code" + '\033[1;90m' + " > " + '\033[0;37m' +f"{CountryC}")
            print('\033[1;93m' + " Postal" + '\033[1;90m' + " > " + '\033[0;37m' +f"{ZIP}")
            print('\033[1;93m' + " TLD" + '\033[1;90m' + " > " + '\033[0;37m' +f"{tld}")
            print('\033[1;93m' + " GPS" + '\033[1;90m' + " > " + '\033[0;37m' +f"{Lat}, {Lon}")
            print('\033[1;93m' + " Timezone" + '\033[1;90m' + " > " + '\033[0;37m' +f"{Time}")
            print('\033[1;93m' + " Currency" + '\033[1;90m' + " > " + '\033[0;37m' +f"{Cur}")
            print('\033[1;93m' + " Reverse" + '\033[1;90m' + " > " + '\033[0;37m' +f"{rever}")
            print('\033[1;93m' + " ORG" + '\033[1;90m' + " > " + '\033[0;37m' +f"{ORG}")
            print('\033[1;93m' + " ISP" + '\033[1;90m' + " > " + '\033[0;37m' +f"{ISP}")
            print('\033[1;93m' + " As" + '\033[1;90m' + " > " + '\033[0;37m' +f"{As}")
            print('\033[1;93m' + " As Name" + '\033[1;90m' + " > " + '\033[0;37m' +f"{Asname}\n")
            
            print('\033[1;93m' + " Mobile" + '\033[1;90m' + " > " + '\033[0;37m' +f"{mob}")
            print('\033[1;93m' + " Proxy" + '\033[1;90m' + " > " + '\033[0;37m' +f"{proxy}")
            print('\033[1;93m' + " Hosting" + '\033[1;90m' + " > " + '\033[0;37m' +f"{hosting}\n")
        if not InfoFromIPAPI_CO:
            print(f"\n\033[1;93m City\033[1;90m:\033[0m {City}")
            print(f"\033[1;93m Region\033[1;90m:\033[0m {Reg}")
            print(f"\033[1;93m Region Name\033[1;90m:\033[0m {RegN}")
            print(f"\033[1;93m Country\033[1;90m:\033[0m {Country}")
            print(f"\033[1;93m Country Code\033[1;90m:\033[0m {CountryC}")
            print(f"\033[1;93m Postal\033[1;90m:\033[0m {ZIP}")
            print(f"\033[1;93m GPS\033[1;90m:\033[0m {Lat}, {Lon}")
            print(f"\033[1;93m Timezone\033[1;90m:\033[0m {Time}")
            print(f"\033[1;93m Currency\033[1;90m:\033[0m {Cur}")
            print(f"\033[1;93m Reverse\033[1;90m:\033[0m {rever}")
            print(f"\033[1;93m ORG\033[1;90m:\033[0m {ORG}")
            print(f"\033[1;93m ISP\033[1;90m:\033[0m {ISP}")
            print(f"\033[1;93m As\033[1;90m:\033[0m {As}")
            print(f"\033[1;93m As Name\033[1;90m:\033[0m {Asname}")

            print(f"\n\033[1;93m Mobile\033[1;90m:\033[0m {mob}")
            print(f"\033[1;93m Proxy\033[1;90m:\033[0m {proxy}")
            print(f"\033[1;93m Hosting\033[1;90m:\033[0m {hosting}")
    else: print(f"\n{bad} Invalid IP\033[0m")