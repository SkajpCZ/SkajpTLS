#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp

def IPLookUp():
    import requests, json
    InfoFromIPAPI_CO = False
    def NULLvals(): Cont = "?"; ContC = "?"; Country = "?"; CountryC = "?"; Reg = "?"; RegN = "?"; City = "?"; Dist = "?"; ZIP = "?"; Lat = "?"; Lon = "?"; Time = "?"; Cur = "?"; ISP = "?"; ORG = "?"; As = "?"; Asname = "?"; rever = "?"; mob = "?"; proxy = "?"; hosting = "?"
    ip = input('\033[1;93m' + "\n Enter IP" + '\033[1;90m' + " > " + '\033[0;37m' +f"")
    url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting"
    r = requests.get(url)
    rj = r.json()
    Status = rj["status"]
    if Status == "success":
        try:
            Cont = rj["continent"]
            ContC = rj["continentCode"]
            Country = rj["country"]
            CountryC = rj["countryCode"]
            Reg = rj["region"]
            RegN = rj["regionName"]
            City = rj["city"]
            Dist = rj["district"]
            ZIP = rj["zip"]
            Lat = rj["lat"]
            Lon = rj["lon"]
            Time = rj["timezone"]
            Cur = rj["currency"]
            ISP = rj["isp"]
            ORG = rj["org"]
            As = rj["as"]
            Asname = rj["asname"]
            rever = rj["reverse"]
            mob = rj["mobile"]
            proxy = rj["proxy"]
            hosting = rj["hosting"]
            try: rj1 = requests.get(f"http://ipapi.co/{ip}/json/").json(); net = rj1["network"]; lang = rj1["languages"]; tld = rj1["country_tld"]; InfoFromIPAPI_CO = True
            except: InfoFromIPAPI_CO = False; NULLvals(); pass
        except Exception as e: print(f"\n\033[1;91m Error: {e}\033[0;37m")
        # Print output
        if InfoFromIPAPI_CO:
            print('\033[1;93m' + "\n Network" + '\033[1;90m' + " > " + '\033[0;37m' +f"{net}")
            print('\033[1;93m' + " City" + '\033[1;90m' + " > " + '\033[0;37m' +f"{City}")
            print('\033[1;93m' + " Languages" + '\033[1;90m' + " > " + '\033[0;37m' +f"{lang}")
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
            print('\033[1;93m' + "\n City" + '\033[1;90m' + " > " + '\033[0;37m' +f"{City}")
            print('\033[1;93m' + " Region" + '\033[1;90m' + " > " + '\033[0;37m' +f"{Reg}")
            print('\033[1;93m' + " Region Name" + '\033[1;90m' + " > " + '\033[0;37m' +f"{RegN}")
            print('\033[1;93m' + " Country" + '\033[1;90m' + " > " + '\033[0;37m' +f"{Country}")
            print('\033[1;93m' + " Country Code" + '\033[1;90m' + " > " + '\033[0;37m' +f"{CountryC}")
            print('\033[1;93m' + " Postal" + '\033[1;90m' + " > " + '\033[0;37m' +f"{ZIP}")
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
    else: print("\n\033[1;91m Invalid IP\033[0;37m")


def old_IPLookUp():
    import requests, json, random
    def nullvalues():
        network = "?"
        city = "?"
        region = "?"
        regcode = "?"
        countryname = "?"
        countrycode = "?"
        countrycap = "?"
        tld = "?"
        contcode = "?"
        postal = "?"
        Lag = "?"
        Long = "?"
        timezone = "?"
        utc_off = "?"
        call = "?"
        cur = "?"
        lang = "?"
        org = "?"
    ip = input('\033[1;93m' + "\n Enter IP" + '\033[1;90m' + " > " + '\033[0;37m' +f"")
    ipinf = f"https://ipapi.co/{ip}/json/"
    stats = requests.get(ipinf)
    json_stats = stats.json()
    try:
        network = json_stats["network"] # 1.1.1.1/24
        city = json_stats["city"] # Sydney
        region = json_stats["region"] # New South Wales
        regcode = json_stats["region_code"] # NSW
        countryname = json_stats["country_name"] # Australia
        countrycode = json_stats["country_code"] # AU
        tld = json_stats["country_tld"] # .au
        contcode = json_stats["continent_code"] # OC
        postal = json_stats["postal"] #2000
        Lag = json_stats["latitude"] # -33.859336
        Long = json_stats["longitude"] # 151.203624
        timezone = json_stats["timezone"] # Australia/Sydney
        utc_off = json_stats["utc_offset"] # +1100
        call = json_stats["country_calling_code"] # +61
        cur = json_stats["currency"] # AUD
        lang = json_stats["languages"] # en-AU
        org = json_stats["asn"] + ", " + json_stats["org"] # AS13335, CLOUDFLARENET
    except KeyError():
        nullvalues()

    headers = [{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}, {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}]
    num = random.randrange(len(headers))
    json_stats1 = requests.get(f"https://vpnapi.io/api/{ip}", headers=headers[int(num)])
    json_stats1.raise_for_status()
    if json_stats1.status_code != 204:
        try:
            req = json_stats1.json()["message"].split(" ")[2]
            if int(req) != 0:
                try:
                    vpn = json_stats1.json()["security"]['vpn']
                    proxy = json_stats1.json()["security"]['proxy']
                    tor = json_stats1.json()["security"]['tor']
                    MesInfo = 'good'
                except KeyError():
                    vpn, proxy, tor = "?"
            else:
                MesInfo = "\033[1;91m Failed to resolve VPN, Proxy, Tor"
        except KeyError():
            vpn, proxy, tor = "?"
    
    print('\033[1;93m' + "\n Network" + '\033[1;90m' + " > " + '\033[0;37m' +f"{network}")
    print('\033[1;93m' + " ORG" + '\033[1;90m' + " > " + '\033[0;37m' +f"{org}")
    print('\033[1;93m' + " TLD" + '\033[1;90m' + " > " + '\033[0;37m' +f"{tld}")
    print('\033[1;93m' + " Languages" + '\033[1;90m' + " > " + '\033[0;37m' +f"{lang}")
    print('\033[1;93m' + " City" + '\033[1;90m' + " > " + '\033[0;37m' +f"{city}")
    print('\033[1;93m' + " Region" + '\033[1;90m' + " > " + '\033[0;37m' +f"{region}")
    print('\033[1;93m' + " Region Code" + '\033[1;90m' + " > " + '\033[0;37m' +f"{regcode}")
    print('\033[1;93m' + " Country Name" + '\033[1;90m' + " > " + '\033[0;37m' +f"{countryname}")
    print('\033[1;93m' + " Country Code" + '\033[1;90m' + " > " + '\033[0;37m' +f"{countrycode}")
    print('\033[1;93m' + " Postal" + '\033[1;90m' + " > " + '\033[0;37m' +f"{postal}")
    print('\033[1;93m' + " GPS" + '\033[1;90m' + " > " + '\033[0;37m' +f"{Lag}, {Long}")
    print('\033[1;93m' + " Timezone" + '\033[1;90m' + " > " + '\033[0;37m' +f"{timezone}")
    print('\033[1;93m' + " Phone" + '\033[1;90m' + " > " + '\033[0;37m' +f"{call}")
    print('\033[1;93m' + " Currency" + '\033[1;90m' + " > " + '\033[0;37m' +f"{cur}\n")
    if MesInfo == 'good':
        print('\033[1;93m' + " VPN" + '\033[1;90m' + " > " + '\033[0;37m' +f"{vpn}")
        print('\033[1;93m' + " Proxy" + '\033[1;90m' + " > " + '\033[0;37m' +f"{proxy}")
        print('\033[1;93m' + " TOR" + '\033[1;90m' + " > " + '\033[0;37m' +f"{tor}\n")
    else:
        print(MesInfo)
