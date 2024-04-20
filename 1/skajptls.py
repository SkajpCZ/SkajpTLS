
#-*- coding: utf-8 -*-

#                Description / Documentation
#                -~=======================~-

# This multi tool was made by Skajp 
# This tool has no comments that will help you with understanding it, or how it works
# So you are on your own, the code isnt very readable also so good luck xd

#                           Usage
#                -~=======================~-

# These are some commands which you can use inside multi tool:
#       - 'help','?','??'   =  help menu
#       - 'opt','options'   =  options menu
#       - 'settings','set'  =  settings of multi tool (working on)
#       - 'clear','cls'     =  Clears terminal
#       - 'credits','cred'  =  Credits to creator
#       - 'exit','quit','e' =  Exit multi tool

# In Submenus
#       - 'back'            =  Back to main menu

# For selecting options you can use commands or numbers
# Example: 
#       Port Scanner
#       'pscan' or '0'


# For colors: https://drive.google.com/drive/u/3/folders/1PxbEodBcZu7z36GPtkRm8itY6jwFcQGB
import os, time

def clear():os.system('cls' if os.name == 'nt' else 'clear')

# Import Modules Made By Skajp
if os.path.exists("./misc"): from misc.modules import windows, kali, termux, pscan, iplookup, mailscrape, obs, proxyscrape, getip, zipcrack, OnlineChat, keylogger, getwifipass, anonftp, maclookup, hashes
else:
    clear()
    print("\n\033[1;91m Failed to locate './misc' folder")
    time.sleep(5)
    quit()


############################### Settings ############################################
def ResetTool():
    print()
    p = '.'
    for i in range(3):
        print('\033[1;31m' + f" Reseting Skajp TLS{p}", end="\r")
        p += '.'
        time.sleep(0.3)
    os.remove("misc/proxies.txt")
    os.remove("misc/.ver")
    shutil.rmtree("misc/chats")
    shutil.rmtree("misc/keylogger/")
    shutil.rmtree("misc/mails")
    shutil.rmtree("misc/wordlists")
    shutil.rmtree("misc/CrackedZips")
    shutil.rmtree("misc/windows")
    shutil.rmtree("misc/modules/__pycache__")
    shutil.rmtree("misc/AnonFiles")
    print('\033[1;31m' + "\n\n Relaunch Skajp TLS to complete reset\033[0;37m")
    time.sleep(3)
    quit()


def PingTesting():
    print()
    if os.name == 'nt':
        print('\033[1;93m' + " Testing \033[1;90m>\033[1;37m Cloudflare", end='\r')
        try: subprocess.check_output("ping 1.1.1.1 -n 1", shell=True);time.sleep(0.1);print('\033[1;92m' + " Success with Cloudflare", end='\r')
        except: time.sleep(0.1);print('\033[1;91m' + " Failed with Cloudflare", end='\r')
        print()
        print('\033[1;93m' + " Testing \033[1;90m>\033[1;37m Cloudflare (Backup Server)", end='\r')
        try: subprocess.check_output("ping 1.0.0.1 -n 1", shell=True);time.sleep(0.1);print('\033[1;92m' + " Success with Cloudflare (Backup Server)", end='\r')
        except: time.sleep(0.1);print('\033[1;91m' + " Failed with Cloudflare (Backup Server)", end='\r')
        print("\n")
        print('\033[1;93m' + " Testing \033[1;90m>\033[1;37m Google", end='\r')
        try: subprocess.check_output("ping 8.8.8.8 -n 1", shell=True);time.sleep(0.1);print('\033[1;92m' + " Success with Google", end='\r')
        except: time.sleep(0.1);print('\033[1;91m' + " Failed with Google", end='\r')
        print()
        print('\033[1;93m' + " Testing \033[1;90m>\033[1;37m Google (Backup Server)", end='\r')
        try: subprocess.check_output("ping 8.8.4.4 -n 1", shell=True);time.sleep(0.1);print('\033[1;92m' + " Success with Google (Backup Server)", end='\r')
        except: time.sleep(0.1);print('\033[1;91m' + " Failed with Google (Backup Server)", end='\r')
        print()
    else:
        print('\033[1;93m' + " Testing \033[1;90m>\033[1;37m Cloudflare", end='\r')
        try: subprocess.check_output("ping -c 1 1.1.1.1", shell=True);time.sleep(0.1);print('\033[1;92m' + " Success with Cloudflare", end='\r')
        except: time.sleep(0.1);print('\033[1;91m' + " Failed with Cloudflare", end='\r')
        print()
        print('\033[1;93m' + " Testing \033[1;90m>\033[1;37m Cloudflare (Backup Server)", end='\r')
        try: subprocess.check_output("ping -c 1 1.0.0.1", shell=True);time.sleep(0.1);print('\033[1;92m' + " Success with Cloudflare (Backup Server)", end='\r')
        except: time.sleep(0.1);print('\033[1;91m' + " Failed with Cloudflare (Backup Server)", end='\r')
        print("\n")
        print('\033[1;93m' + " Testing \033[1;90m>\033[1;37m Google", end='\r')
        try: subprocess.check_output("ping -c 1 8.8.8.8", shell=True);time.sleep(0.1);print('\033[1;92m' + " Success with Google", end='\r')
        except: time.sleep(0.1);print('\033[1;91m' + " Failed with Google", end='\r')
        print()
        print('\033[1;93m' + " Testing \033[1;90m>\033[1;37m Google (Backup Server)", end='\r')
        try: subprocess.check_output("ping -c 1 8.8.4.4", shell=True);time.sleep(0.1);print('\033[1;92m' + " Success with Google (Backup Server)", end='\r')
        except: time.sleep(0.1);print('\033[1;91m' + " Failed with Google (Backup Server)", end='\r')
        print()


def CheckUpdates():
    if os.name == 'nt':
        try: subprocess.check_output("ping 1.1.1.1 -n 1", shell=True); conec = 1
        except: conec = 0
    else:
        try: subprocess.check_output("ping -c 1 1.1.1.1", shell=True); conec = 1
        except: conec = 0
    if conec == 1: response = requests.get('https://pastebin.com/raw/Y4fBQP1h')
    elif conec == 0: print('\033[1;31m' + "\n No internet connection")
    if int(tlsver) == int(response.text): print('\033[1;32m' + "\n Up to date")
    elif int(tlsver) > int(response.text): print('\033[1;34m' + "\n Newer (testing)")
    else: print('\033[1;31m' + "\n Old")

def get_misc_size():
    total_size = 0
    for dirpath, dirnames, filenames in os.walk('./misc/'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    total_size = ('{:,}'.format(int(total_size)))
    return total_size


def ChangeLogoStyle(a):
    PathToSettings = "./misc/settings/settings.json"
    if a == "logo_type":
        with open(PathToSettings, 'r') as f: data = json.load(f)

        if data['logo_type'] == "random": ltype = 'static'
        if data['logo_type'] == "static": ltype = 'random'
        data['logo_type'] = ltype

        with open(PathToSettings, 'w') as f: json.dump(data, f)
    elif a == "colors":
        with open(PathToSettings, 'r') as f: data = json.load(f)
        r = data['static-colors']['r']
        g = data['static-colors']['g']
        b = data['static-colors']['b']

        print(f" \033[1;92m R \033[1;90m> \033[1;37m{r}")
        print(f" \033[1;91m G \033[1;90m> \033[1;37m{g}")
        print(f" \033[1;94m B \033[1;90m> \033[1;37m{b}")

        print("  \n\033[1;93m New values\033[1;90m:\n")

        r = input(f" \033[1;91m R \033[1;90m> \033[1;37m")
        g = input(f" \033[1;92m G \033[1;90m> \033[1;37m")
        b = input(f" \033[1;94m B \033[1;90m> \033[1;37m")

        data['static-colors']['r'] = r
        data['static-colors']['g'] = g
        data['static-colors']['b'] = b

        with open(PathToSettings, 'w') as f: json.dump(data, f)



############################### Settings ############################################

#################################################################################################
######################################## Submenus ###############################################
#################################################################################################

def webs_submenu():
    tW = 1 if os.path.exists("/data/data/com.termux") else 0
    while True:
        cho = input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mWebs\033[0;37m) \033[1;31mNT \033[1;90m> \033[0;37m").lower() if os.name == 'nt' else input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mWebs\033[0;37m) \033[1;90m> \033[0;37m").lower()
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: menu()
        elif cho in ['opt', 'options']: webs_manual()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['credits', 'cred']: Credits()
        # Commands
        elif cho in ["fakename","0"]: webbrowser.open("https://www.fakenamegenerator.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.fakenamegenerator.com/")
        elif cho in ["vedbex","1"]: webbrowser.open("https://www.vedbex.com/tools/home"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.vedbex.com/tools/home")
        elif cho in ["ascii","2"]: webbrowser.open("https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=SkajpTLS"); webbrowser.open("https://ascii.co.uk/art"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=SkajpTLS\n https://ascii.co.uk/art")
        elif cho in ["fonts","3"]: webbrowser.open("https://www.messletters.com/en/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.messletters.com/en/")
        elif cho in ["bugcrowd","4"]: webbrowser.open("https://bugcrowd.com/programs"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://bugcrowd.com/programs")
        elif cho in ["malwaredb","5"]: webbrowser.open("https://github.com/Endermanch/MalwareDatabase"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://github.com/Endermanch/MalwareDatabase")
        elif cho in ["tineye","6"]: webbrowser.open("https://tineye.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://tineye.com/")
        elif cho in ["pwned","7"]: webbrowser.open("https://haveibeenpwned.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://haveibeenpwned.com/")
        elif cho in ["pyobs","8"]: webbrowser.open("https://pyob.oxyry.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://pyob.oxyry.com/")
        elif cho in ["passposs","9"]: webbrowser.open("http://www.csgnetwork.com/optionspossiblecalc.html"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n http://www.csgnetwork.com/optionspossiblecalc.html")
        elif cho in ["lullar","10"]: webbrowser.open("https://com.lullar.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://com.lullar.com/")
        elif cho in ["virustotal","11"]: webbrowser.open("https://www.virustotal.com"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.virustotal.com")
        elif cho in ["metaread","12"]: webbrowser.open("https://www.metadata2go.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.metadata2go.com/")
        elif cho in ["py2to3","13"]: webbrowser.open("https://python2to3.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://python2to3.com/")
        elif cho in ["cookieconv","14"]: webbrowser.open("https://www.cookieconverter.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.cookieconverter.com/")
        elif cho in ["portapps","15"]: webbrowser.open("https://portableapps.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://portableapps.com/")
        elif cho in ["photosherlock","16"]: webbrowser.open("https://photosherlock.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + " https://photosherlock.com/")
        elif cho in ["etools","17"]: webbrowser.open("https://www.etools.ch/searchAdvanced.do"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.etools.ch/searchAdvanced.do")
        elif cho in ["webarchive","18"]: webbrowser.open("https://web.archive.org/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://web.archive.org/")
        elif cho in ["stackoverflow","19"]: webbrowser.open("https://stackoverflow.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://stackoverflow.com/")
        elif cho in ["deepl","20"]: webbrowser.open("https://www.deepl.com/translator"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.deepl.com/translator")
        elif cho in ["cloudconv","21"]: webbrowser.open("https://cloudconvert.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://cloudconvert.com/")
        elif cho in ["canarytokens","22"]: webbrowser.open("https://canarytokens.org/generate"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://canarytokens.org/generate")
        elif cho in ["pimeyes","23"]: webbrowser.open("https://pimeyes.com/en"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://pimeyes.com/en")
        elif cho in ["inseccam","24"]: webbrowser.open("http://insecam.org/en/bytype/WebcamXP/?page=1"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n http://insecam.org/en/bytype/WebcamXP/?page=1")
        elif cho in ["keyboardcodes","25"]: webbrowser.open("https://www.toptal.com/developers/keycode"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.toptal.com/developers/keycode")
        elif cho in ["snapmap","26"]: webbrowser.open("https://map.snapchat.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://map.snapchat.com/")
        elif cho in ["shodan","27"]: webbrowser.open("https://www.shodan.io/dashboard"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.shodan.io/dashboard")
        elif cho in ["tempmail","28"]: webbrowser.open("https://tempmail.email/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://tempmail.email/")
        elif cho in ["explainshell","29"]: webbrowser.open("https://explainshell.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://explainshell.com/")
        elif cho in ["bashupload","30"]: webbrowser.open("https://bashupload.com/how_to_upload_file_to_server"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://bashupload.com/how_to_upload_file_to_server")
        elif cho in ["secpass","31"]: webbrowser.open("https://www.security.org/how-secure-is-my-password/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.security.org/how-secure-is-my-password/")
        elif cho in ["gtfobins","32"]: webbrowser.open("https://gtfobins.github.io/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://gtfobins.github.io/")
        elif cho in ["cyberchef","33"]: webbrowser.open("https://gchq.github.io/CyberChef/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://gchq.github.io/CyberChef/")
        elif cho in ["sms","34"]: webbrowser.open("https://receive-smss.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://receive-smss.com/")
        elif cho in ["spok","35"]: webbrowser.open("https://www.spokeo.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.spokeo.com/")
        elif cho in ["ath","36"]: webbrowser.open("https://www.asciitohex.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.asciitohex.com/")
        elif cho in ["aperi","37"]: webbrowser.open("https://www.aperisolve.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.aperisolve.com/")
        elif cho in ["dcode","38"]: webbrowser.open("https://www.dcode.fr/en"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.dcode.fr/en")
        elif cho in ["penm","39"]: webbrowser.open("https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet")
        elif cho in ["hashi","40"]: webbrowser.open("https://hashes.com/en/tools/hash_identifier"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://hashes.com/en/tools/hash_identifier")
        elif cho in ["dechash","41"]: webbrowser.open("https://md5decrypt.net/en/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://md5decrypt.net/en/")
        elif cho in ["m5calc","42"]: webbrowser.open("https://md5calc.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://md5calc.com/")
        elif cho in ["mailspoof","43"]: webbrowser.open("https://emkei.cz/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://emkei.cz/")
        elif cho in ["rockstar","44"]: webbrowser.open("https://codewithrockstar.com/online"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://codewithrockstar.com/online")
        elif cho in ["exifer","45"]: webbrowser.open("https://www.thexifer.net/#"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://www.thexifer.net/#")
        elif cho in ["wcalld","46"]: webbrowser.open("https://whocalld.com/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://whocalld.com/")
        elif cho in ["itech","47"]: webbrowser.open("https://inteltechniques.com/tools/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://inteltechniques.com/tools/")
        elif cho in ["crack","48"]: webbrowser.open("https://crackstation.net/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://crackstation.net/")
        elif cho in ["facecheck","49"]: webbrowser.open("https://facecheck.id/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://facecheck.id/")
        else:
            if os.name == 'nt':
                winc = ["ipconfig","dir","echo","ping","whoami","cd","start"]
                try:
                    if cho in winc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")
            else:
                lc = ["searchsploit","ifconfig","msfconsole","nmap","ls","cd","cat","sudo","apt","echo","ping","whoami","uname","mdkir","rm","pwd","touch","nano","vim","service","systemctl","ip"]
                try:
                    if cho in lc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")

def Settings_menu():
    while True:
        cho = input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mSettings\033[0;37m) \033[1;31mNT \033[1;90m> \033[0;37m").lower() if os.name == 'nt' else input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mSettings\033[0;37m) \033[1;90m> \033[0;37m").lower()
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        # Misc Options
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: menu()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['credits', 'cred']: Credits()
        elif cho in ['opt', 'options']: settings_manual()
        # Commands
        elif cho in ['reset', '0']: ResetTool()
        elif cho in ['internet','ping', '1']: PingTesting()
        elif cho in ['updates','checkup','ups','update', '2']: CheckUpdates()
        elif cho in ['msize', 'misc', 'miscsize', '3']: print(f"\n\033[1;93m Size of \033[1;37m./misc \033[0;90m> \033[1;37m{get_misc_size()}\033[1;90m bytes")
        elif cho in ['colors', '4']: SettingsColors_menu()
        else:
            if os.name == 'nt':
                winc = ["ipconfig","dir","echo","ping","whoami","cd","start"]
                try:
                    if cho in winc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")
            else:
                lc = ["searchsploit","ifconfig","msfconsole","nmap","ls","cd","cat","sudo","apt","echo","ping","whoami","uname","mdkir","rm","pwd","touch","nano","vim","service","systemctl","ip"]
                try:
                    if cho in lc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")

def SettingsColors_menu():
    while True:
        cho = input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mSettings/Colors\033[0;37m) \033[1;31mNT \033[1;90m> \033[0;37m").lower() if os.name == 'nt' else input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mSettings/Colors\033[0;37m) \033[1;90m> \033[0;37m").lower()
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        # Misc Options
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: Settings_menu()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['credits', 'cred']: Credits()
        elif cho in ['opt', 'options']: settingsColors_manual()
        # Commands
        elif cho in ['ltype', '0']: ChangeLogoStyle("logo_type")
        elif cho in ['chcol', '1']: ChangeLogoStyle("colors")
        else:
            if os.name == 'nt':
                winc = ["ipconfig","dir","echo","ping","whoami","cd","start"]
                try:
                    if cho in winc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")
            else:
                lc = ["searchsploit","ifconfig","msfconsole","nmap","ls","cd","cat","sudo","apt","echo","ping","whoami","uname","mdkir","rm","pwd","touch","nano","vim","service","systemctl","ip"]
                try:
                    if cho in lc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")


def windows_submenu():
    while True:
        cho = input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mWindows\033[0;37m) \033[1;90m> \033[0;37m").lower()
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        # Misc Options
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: menu()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['credits', 'cred']: Credits()
        elif cho in ['opt', 'options']: windows_submenu_manual()
        # Commands
        elif cho in ['wifi', '0']: print(); getwifipass.GetWifiPass()
        elif cho in ['gpedit','1']: windows.EnableGPEDIT() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['wifiadapt', '2']: windows.GWA()
        elif cho in ['powerplan', 'plans','3']: PowerPlansMenu()
        elif cho in ['us', 'soft', 'software','4']: print("Working on") #UsefulSoftware() if InChck() else print("\033[1;31m\n No internet connection")
        else:
            if os.name == 'nt':
                winc = ["ipconfig","dir","echo","ping","whoami","cd","start"]
                try:
                    if cho in winc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")
            else:
                lc = ["searchsploit","ifconfig","msfconsole","nmap","ls","cd","cat","sudo","apt","echo","ping","whoami","uname","mdkir","rm","pwd","touch","nano","vim","service","systemctl","ip"]
                try:
                    if cho in lc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")

def kalilinux_submenu():
    while True:
        cho = input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mKali Linux\033[0;37m) \033[1;90m> \033[0;37m").lower()
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: menu()
        elif cho in ['opt', 'options']: kalilinux_submenu_manual()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['credits', 'cred']: Credits()
        # Commands
        elif cho in ['fullupgrade', '0']: os.system("sudo apt clean -y && sudo apt update -y && sudo apt list --upgradable && sudo apt upgrade -y && sudo apt autoremove -y") if CheckForNet() == True else os.system("sudo apt clean -y && sudo apt update -y && sudo apt list --upgradable && sudo apt upgrade -y && sudo apt autoremove -y") if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['large','1']: os.system("sudo apt install kali-linux-large -y") if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['full','2']: os.system("sudo apt install kali-linux-everything -y") if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['atom','3']: KaliAtom() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['ngrok','4']: KaliNgrok() if InChck() else print("\033[1;31m\n No internet connection")
        else:
            if os.name == 'nt':
                winc = ["ipconfig","dir","echo","ping","whoami","cd","start"]
                try:
                    if cho in winc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")
            else:
                lc = ["searchsploit","ifconfig","msfconsole","nmap","ls","cd","cat","sudo","apt","echo","ping","whoami","uname","mdkir","rm","pwd","touch","nano","vim","service","systemctl","ip"]
                try:
                    if cho in lc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")

def termux_submenu():
    while True:
        cho = input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mTermux\033[0;37m) \033[1;90m> \033[0;37m").lower()
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: menu()
        elif cho in ['opt', 'options']: termux_submenu_manual()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['credits', 'cred']: Credits()
        # Commands
        elif cho in ['kali','linux','kalilinux','nethunter']: os.system("chmod +x ./misc/termux/install-kali && ./misc/termux/install-kali")
        elif cho in ['repositories','repos','repo']: os.system("pkg install root-repo x11-repo -y")
        elif cho in ['storage','setup-storage']: os.system("setup-termux-storage")
        elif cho in ['thchydra','thch']: print('\033[1;31m' + "\n Working on...") #os.system("chmod +x ./misc/termux/hydra && ./misc/termux/hydra")
        else:
            if os.name == 'nt':
                winc = ["ipconfig","dir","echo","ping","whoami","cd","start"]
                try:
                    if cho in winc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")
            else:
                lc = ["searchsploit","ifconfig","msfconsole","nmap","ls","cd","cat","sudo","apt","echo","ping","whoami","uname","mdkir","rm","pwd","touch","nano","vim","service","systemctl","ip"]
                try:
                    if cho in lc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")

def hash_submenu():
    while True:
        cho = input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mHashing\033[0;37m) \033[1;31mNT \033[1;90m> \033[0;37m").lower() if os.name == 'nt' else input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mHashing\033[0;37m) \033[1;90m> \033[0;37m").lower()
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        # Misc Options
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: menu()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['credits', 'cred']: Credits()
        elif cho in ['opt', 'options']: hashing_submenu_manual()
        # Commands
        elif cho in ['md5', '0']: hashes.hashing("md5")
        elif cho in ['sha1','1']: hashes.hashing("sha1")
        elif cho in ['sha224','2']: hashes.hashing("sha224")
        elif cho in ['sha256','3']: hashes.hashing("sha256")
        elif cho in ['sha384','4']: hashes.hashing("sha384")
        elif cho in ['sha512','5']: hashes.hashing("sha512")
        else:
            if os.name == 'nt':
                winc = ["ipconfig","dir","echo","ping","whoami","cd","start"]
                try:
                    if cho in winc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")
            else:
                lc = ["searchsploit","ifconfig","msfconsole","nmap","ls","cd","cat","sudo","apt","echo","ping","whoami","uname","mdkir","rm","pwd","touch","nano","vim","service","systemctl","ip"]
                try:
                    if cho in lc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")

def Wlist_submenu():
    while True:
        cho = input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mWordlists\033[0;37m) \033[1;90m> \033[0;37m").lower()
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        # Misc Options
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: menu()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['credits', 'cred']: Credits()
        elif cho in ['opt', 'options']: wlists_submenu_manual()
        # Commands
        elif cho in ['rockyou', '0']: DownWordlists.Dwordl("rockyou")
        elif cho in ['small', '1']: DownWordlists.Dwordl("md5small")
        elif cho in ['big', '2']: DownWordlists.Dwordl("md5BIG")
        elif cho in ['bigone', '3']: DownWordlists.Dwordl("Bigone")
        elif cho in ['crackdown', '4']: DownWordlists.Dwordl("Crackdown")
        elif cho in ['insider', '5']: DownWordlists.Dwordl("Insider")
        elif cho in ['major', '6']: DownWordlists.Dwordl("Major")
        elif cho in ['neo', '7']: DownWordlists.Dwordl("Neo")
        elif cho in ['potential', '8']: DownWordlists.Dwordl("Potential")
        elif cho in ['ransom', '9']: DownWordlists.Dwordl("Ransom")
        else:
            if os.name == 'nt':
                winc = ["ipconfig","dir","echo","ping","whoami","cd","start"]
                try:
                    if cho in winc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")
            else:
                lc = ["searchsploit","ifconfig","msfconsole","nmap","ls","cd","cat","sudo","apt","echo","ping","whoami","uname","mdkir","rm","pwd","touch","nano","vim","service","systemctl","ip"]
                try:
                    if cho in lc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")

def chat_submenu(): OnlineChat.Menu(); menu()

#########################################################################################################
######################################## Windows Submenus ###############################################
#########################################################################################################
def PowerPlansMenu():
    while True:
        cho = input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mWindows/Power Plans\033[0;37m) \033[1;90m> \033[0;37m").lower()
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        # Misc Options
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: windows_submenu()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['credits', 'cred']: Credits()
        elif cho in ['opt', 'options']: windows_powerplan_submenu_manual()
        # Commands
        elif cho in ['ultimate','0']: windows.UPP()
        elif cho in ['balanced','1']: windows.BPP()
        elif cho in ['saver','2']: windows.PPP()
        else:
            if os.name == 'nt':
                winc = ["ipconfig","dir","echo","ping","whoami","cd","start"]
                try:
                    if cho in winc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")
            else:
                lc = ["searchsploit","ifconfig","msfconsole","nmap","ls","cd","cat","sudo","apt","echo","ping","whoami","uname","mdkir","rm","pwd","touch","nano","vim","service","systemctl","ip"]
                try:
                    if cho in lc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")

def UsefulSoftware():
    while True:
        cho = input("\n \033[1m\033[4;37mskajptls\033[0m (\033[4;38;2;200;127;0mWindows/Useful Software\033[0;37m) \033[1;90m> \033[0;37m").lower()
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        # Misc Options
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: windows_submenu()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['credits', 'cred']: Credits()
        elif cho in ['opt', 'options']: windows_software_submenu_manual()
        # Commands
        elif cho in ['putty', '0']: installsoftware.InstallSoft("Putty")
        elif cho in ['winscp', '1']: installsoftware.InstallSoft("WinSCP")
        elif cho in ['proc', '2']: installsoftware.InstallSoft("ProcHacker")
        elif cho in ['winaero', '3']: installsoftware.InstallSoft("Winaero")
        elif cho in ['last', '4']: installsoftware.InstallSoft("LastActivityView")
        elif cho in ['wiztree', '5']: installsoftware.InstallSoft("Wiztree")
        elif cho in ['untool', '6']: installsoftware.InstallSoft("UninstallSoft")
        elif cho in ['hxd', '7']: installsoftware.InstallSoft("HxD")
        elif cho in ['vlc', '8']: installsoftware.InstallSoft("VLC")
        elif cho in ['obs', '9']: installsoftware.InstallSoft("OBS")
        elif cho in ['audacity', '10']: installsoftware.InstallSoft("Audacity")
        elif cho in ['islc', '11']: installsoftware.InstallSoft("ISLC")
        elif cho in ['hwinf', '12']: installsoftware.InstallSoft("HWinfo")
        elif cho in ['sandboxie', '13']: installsoftware.InstallSoft("Sandboxie")
        elif cho in ['handbrake', '14']: installsoftware.InstallSoft("HandBrake")
        elif cho in ['winrar', '15']: installsoftware.InstallSoft("Winrar")
        elif cho in ['7zip', '16']: installsoftware.InstallSoft("7zip")
        elif cho in ['rufus', '17']: installsoftware.InstallSoft("Rufus")
        elif cho in ['etcher', '18']: installsoftware.InstallSoft("Etch")
        elif cho in ['ghidra', '19']: installsoftware.InstallSoft("Ghidra")
        elif cho in ['x64dbg', '20']: installsoftware.InstallSoft("x64dbg")
        elif cho in ['vbox', '21']: installsoftware.InstallSoft("Vbox")
        elif cho in ['vmw', '22']: installsoftware.InstallSoft("VMw")
        elif cho in ['hash', '23']: installsoftware.InstallSoft("hash")
        elif cho in ['wire', '24']: installsoftware.InstallSoft("Wire")
        elif cho in ['codium', '25']: installsoftware.InstallSoft("Cod")
        elif cho in ['nmap', '26']: installsoftware.InstallSoft("Nmap")
        elif cho in ['die', '27']: installsoftware.InstallSoft("DIE")
        elif cho in ['peid', '28']: installsoftware.InstallSoft("Peid")

        else:
            if os.name == 'nt':
                winc = ["ipconfig","dir","echo","ping","whoami","cd","start"]
                try:
                    if cho in winc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")
            else:
                lc = ["searchsploit","ifconfig","msfconsole","nmap","ls","cd","cat","sudo","apt","echo","ping","whoami","uname","mdkir","rm","pwd","touch","nano","vim","service","systemctl","ip"]
                try:
                    if cho in lc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")




#################################################################################################
######################################## Submenus ###############################################
#################################################################################################



################################################################################################
######################################## Manuals ###############################################
################################################################################################
def help_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"
    table = PrettyTable()
    data = [[NameCol + "Options", CommandCol + "opt", InfoCol + "Shows every option of skajp tools" + TableCol],
            [NameCol + "Settings", CommandCol + "settings", InfoCol + "Shows settings of skajp tools" + TableCol],
            [NameCol + "Help", CommandCol + "help", InfoCol + "Shows this menu" + TableCol],
            [NameCol + "Clear", CommandCol + "cls", InfoCol + "Clears terminal" + TableCol],
            [NameCol + "Credits", CommandCol + "credits", InfoCol + "Credits" + TableCol],
            [NameCol + "Exit", CommandCol + "exit", InfoCol + "Exits tool" + TableCol]]
    table.field_names = ["+", "\033[4;37mHelp\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row(['x'] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")

def helpsub_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    table = PrettyTable()
    data = [[NameCol + "Options", CommandCol + "opt", InfoCol + "Shows every option of skajp tools" + TableCol],
            [NameCol + "Settings", CommandCol + "settings", InfoCol + "Shows settings of skajp tools" + TableCol],
            [NameCol + "Back", CommandCol + "back", InfoCol + "Goes back to main menu" + TableCol],
            [NameCol + "Help", CommandCol + "help", InfoCol + "Shows this menu" + TableCol],
            [NameCol + "Clear", CommandCol + "cls", InfoCol + "Clears terminal" + TableCol],
            [NameCol + "Credits", CommandCol + "credits", InfoCol + "Credits" + TableCol],
            [NameCol + "Exit", CommandCol + "exit", InfoCol + "Exits tool" + TableCol]]
    table.field_names = ["+", "\033[4;37mHelp\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row(['x'] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")

def options_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    table = PrettyTable()
    data = [[NameCol + "Port Scanner", CommandCol + "pscan", InfoCol + "Scans ports on specified target" + TableCol],
            [NameCol + "Geo IP", CommandCol + "geoip", InfoCol + "Shows basic info about IP" + TableCol],
            [NameCol + "Mac Lookup", CommandCol + "mac", InfoCol + "Shows basic info about mac address" + TableCol],
            [NameCol + "My IP", CommandCol + "myip", InfoCol + "Shows your public and private ip" + TableCol],
            [NameCol + "Anonymous FTP", CommandCol + "aftp", InfoCol + "Tries anonymous login on ftp server" + TableCol],]
    table.field_names = ["+", "\033[4;37mNetwork\033[0;37m \033[4;38;2;170;190;254mOptions" + TableCol ,"\033[4;38;2;150;170;234mCommand" + TableCol,"\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+0] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table)

    table = PrettyTable()
    data = [[NameCol + "Mail Scraper", CommandCol + "mailscraper", InfoCol + "Scrapes mails from website" + TableCol],
            [NameCol + "Proxy Scraper", CommandCol + "proxies", InfoCol + "Scrapes proxies" + TableCol]]
    table.field_names = ["+", "\033[4;37mScraper\033[0;37m \033[4;38;2;170;190;254mOptions" + TableCol,"\033[4;38;2;150;170;234mCommand" + TableCol,"\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+5] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table)

    table = PrettyTable()
    data = [[NameCol + "Chat Server", CommandCol + "chat", InfoCol + "Starts a chat server that people can connect to" + TableCol],
            [NameCol + "Zip Cracker", CommandCol + "zipcrack", InfoCol + "Script that can crack .zip files" + TableCol],
            [NameCol + "Python Obfuscation", CommandCol + "pyobs", InfoCol + "Strong python obfuscation" + TableCol],
            [NameCol + "Keylogger", CommandCol + "keylog", InfoCol + "Starts keylogger server and creates client for it" + TableCol],]
    table.field_names = ["+", "\033[4;37mMisc\033[0;37m \033[4;38;2;170;190;254mOptions" + TableCol,"\033[4;38;2;150;170;234mCommand" + TableCol,"\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+7] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table)

    table = PrettyTable()
    data = [[NameCol + "Windows", CommandCol + "windows", InfoCol + "Some useful tools for windows" + TableCol],
            [NameCol + "Kali Linux", CommandCol + "kali", InfoCol + "Some useful tools for kali linux" + TableCol],
            [NameCol + "Termux", CommandCol + "termux", InfoCol + "Some useful tools for termux" + TableCol],
            [NameCol + "Webs", CommandCol + "webs", InfoCol + "Some useful webs" + TableCol],
            [NameCol + "Hashing", CommandCol + "hash", InfoCol + "Encode string to some hashes" + TableCol],
            [NameCol + "Wordlists", CommandCol + "wlists", InfoCol + "Can download some wordlsists" + TableCol]]
    table.field_names = ["+", "\033[4;37mSubmenus\033[0;37m \033[4;38;2;170;190;254mOptions" + TableCol,"\033[4;38;2;150;170;234mCommand" + TableCol,"\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+11] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")

    print("\033[1;38;2;160;140;180m More options will be available in the future")

def webs_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    table = PrettyTable()
    data = [[NameCol + "Fake Name Generator", CommandCol + "fakename", InfoCol + "Generates random person info" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Vedbex", CommandCol + "vedbex", InfoCol + "Multi tool in web" + "\033[0;38;2;50;50;50m"],
            [NameCol + "ASCII Art", CommandCol + "ascii", InfoCol + "Opens 2 sites with ASCII art" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Fancy Fonts", CommandCol + "fonts", InfoCol + "You can make fancy font here" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Bugcrowd", CommandCol + "bugcrowd", InfoCol + "You can get money from finding bugs in webs" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Malware Database", CommandCol + "malwaredb", InfoCol + "Github repo with some malwares" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Tineye", CommandCol + "tineye", InfoCol + "Image analyzer" + "\033[0;38;2;50;50;50m"],
            [NameCol + "haveibeenpwned", CommandCol + "pwned", InfoCol + "Tells you if you are in some leaked db" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Python Obsfucator", CommandCol + "pyobs", InfoCol + "Obsfucates python code" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Password Possibilities", CommandCol + "passposs", InfoCol + "Calculates how many possible can be with custom parameters" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Lullar", CommandCol + "lullar", InfoCol + "OSINT tool" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Virustotal", CommandCol + "virustotal", InfoCol + "Examines file with vms and avs" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Metadata Reader", CommandCol + "metaread", InfoCol + "Reads metadata from file" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Python 2 To 3 Convertor", CommandCol + "py2to3", InfoCol + "Converts python 2 code to python 3 code" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Cookie Convertor", CommandCol + "cookieconv", InfoCol + "Converts netscape cookie to json cookie" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Portable Apps", CommandCol + "portapps", InfoCol + "You can download some portable apps" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Photosherlock", CommandCol + "photosherlock", InfoCol + "Another image analyzer" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Etools", CommandCol + "etools", InfoCol + "Multi tool in web" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Webarchive", CommandCol + "webarchive", InfoCol + "You can find some archived webs on there" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Stackoverflow", CommandCol + "stackoverflow", InfoCol + "Biggest forum for programers" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Deepl Translator", CommandCol + "deepl", InfoCol + "Something like google translator" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Cloud Convert", CommandCol + "cloudconv", InfoCol + "You can convert file to other format" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Canary Tokens", CommandCol + "canarytokens", InfoCol + "You can create file with ip grabber" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Pimeyes", CommandCol + "pimeyes", InfoCol + "Another image analyzer" + "\033[0;38;2;50;50;50m"],
            [NameCol + "InsecCam", CommandCol + "inseccam", InfoCol + "Shows cameras that are open to the web" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Keyboard Codes", CommandCol + "keyboardcodes", InfoCol + "Can show you what code has key on keyboard" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Snapchat Map", CommandCol + "snapmap", InfoCol + "This site shows you snapchat map" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Shodan", CommandCol + "shodan", InfoCol + "This site shows devices that have opened ports to the internet" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Temp Mail", CommandCol + "tempmail", InfoCol + "This site creates temp mail for random register" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Explain Shells", CommandCol + "explainshell", InfoCol + "This site will explain any shell command" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Bash Upload", CommandCol + "bashupload", InfoCol + "This site allows you to share files that have 50GB for 3 days" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Security.org", CommandCol + "secpass", InfoCol + "This site shows you how strong password you have" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Gtfobins", CommandCol + "gtfobins", InfoCol + "Some interessting commands for linux" + "\033[0;38;2;50;50;50m"],
            [NameCol + "CyberChef", CommandCol + "cyberchef", InfoCol + "One of the best for encryption/decryption" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Recieve SMS", CommandCol + "sms", InfoCol + "You can recieve sms on anonymous number" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Spokeo", CommandCol + "spok", InfoCol + "You can search for people here" + "\033[0;38;2;50;50;50m"],
            [NameCol + "AnsiiToHex", CommandCol + "ath", InfoCol + "Some site for cryptography" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Aperisolve", CommandCol + "aperi", InfoCol + "This site allows you to do simple stego on images" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Dcode", CommandCol + "dcode", InfoCol + "You can find lot of cypher, analyzers and more" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Pentestmonkey", CommandCol + "penm", InfoCol + "Some reverse shell commands" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Hash Identify", CommandCol + "hashi", InfoCol + "Identify almost any hash on this site" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Decode Hash", CommandCol + "dechash", InfoCol + "You can try decoding some hashes here" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Md5 Calc", CommandCol + "m5calc", InfoCol + "You can find some tools here" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Mail Spoofer", CommandCol + "mailspoof", InfoCol + "You can send spoofed emails" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Rockstar", CommandCol + "rockstar", InfoCol + "Lyrics can be translated to code" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Exifer", CommandCol + "exifer", InfoCol + "Website for exif data" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Whocalld", CommandCol + "wcalld", InfoCol + "Some info about telephone number" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Intel Techniques", CommandCol + "itech", InfoCol + "Some nice tools for osint" + "\033[0;38;2;50;50;50m"],
            [NameCol + "Crack Station", CommandCol + "crack", InfoCol + "Database of hashes" + "\033[0;38;2;50;50;50m"],
            ]


    table.field_names = ["+", "\033[4;38;2;170;190;254mOptions\033[0;30m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+0] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")
    print("\033[1;38;2;160;140;180m To go back type \033[4;38;2;190;180;200mback\033[0;37m")

def settings_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    table = PrettyTable()
    data = [[NameCol + "Reset Skajp TLS", CommandCol + "reset", InfoCol + "Resets all things in this tool" + TableCol],
            [NameCol + "Test Internet", CommandCol + "ping", InfoCol + "Pings couple servers for response" + TableCol],
            [NameCol + "Check Updates", CommandCol + "update", InfoCol + "Check updates fro Skajp TLS" + TableCol],
            [NameCol + "Size Of ./misc", CommandCol + "msize", InfoCol + "Shows you size in bytes of ./misc folder" + TableCol],]
    table.field_names = ["+", "\033[4;37mSettings\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+0] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")
    table = PrettyTable()
    data = [[NameCol + "Color Of Logo", CommandCol + "colors", InfoCol + "Allows you to change mode or rgb values of logo" + TableCol],]
    table.field_names = ["+", "\033[0m\033[4;37mSubmenus\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+4] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")
    print("\033[1;38;2;160;140;180m To go back type \033[4;38;2;190;180;200mback\033[0;37m")

def settingsColors_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    PathToSettings = "./misc/settings/settings.json"

    with open(PathToSettings, 'r') as f:
        data = json.load(f)
    logo_type = data["logo_type"]
    logoType = "\033[1;92m" if logo_type == "static" else "\033[1;96m"
    table = PrettyTable()
    data = [[NameCol + "Logo Type", f"{logoType}{logo_type}" , CommandCol + "ltype", InfoCol + "Changes logo type between static and random" + TableCol],
            [NameCol + "Change Colors", "\033[1;91mR\033[1;92mG\033[1;94mB" , CommandCol + "chcol", InfoCol + "Change static rgb values" + TableCol],]
    table.field_names = ["+", "\033[4;37mSettings\033[0;37m \033[4;38;2;170;190;254mColors\033[0;30m", "\033[4;38;2;140;160;224mType\033[0;37m", "\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+0] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")
    print("\033[1;38;2;160;140;180m To go back type \033[4;38;2;190;180;200mback\033[0;37m")


def windows_submenu_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    table = PrettyTable()
    data = [[NameCol + "Wifi Passwords", CommandCol + "wifi", InfoCol + "Shows saved wifi passwords in your pc" + TableCol],
            [NameCol + "Group Policy Editor", CommandCol + "gpedit", InfoCol + "Enables gpedit.msc on home version of windows" + TableCol],
            [NameCol + "Wifi Adpater", CommandCol + "wifiadapt", InfoCol + "Checks capabilities of your wifi card" + TableCol],]
    table.field_names = ["+", "\033[4;37mWindows\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+0] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")

    table = PrettyTable()
    data = [[NameCol + "Power plans", CommandCol + "plans", InfoCol + "Creates power plans for windows" + TableCol],
            [NameCol + "Useful Software", CommandCol + "soft", InfoCol + "Some useful software for windows" + TableCol],]
    table.field_names = ["+", "\033[0m\033[4;37mSubmenus\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+3] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")
    print("\033[1;38;2;160;140;180m To go back type \033[4;38;2;190;180;200mback\033[0;37m")

def kalilinux_submenu_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    table = PrettyTable()
    data = [[NameCol + "Full Upgrade", CommandCol + "fullupgrade", InfoCol + "Updates and upgrades all things in kali" + TableCol],
            [NameCol + "Kali Large", CommandCol + "large", InfoCol + "Pack of tools in kali (it was in installer, now it isn't)" + TableCol],
            [NameCol + "Kali Everything", CommandCol + "full", InfoCol + "Pack of almost every tool in kali" + TableCol],
            [NameCol + "Atom Editor", CommandCol + "atom", InfoCol + "Installs atom text editor" + TableCol],
            [NameCol + "Ngrok", CommandCol + "ngrok", InfoCol + "Installs ngrok" + TableCol]]
    table.field_names = ["+", "\033[4;37mKali Linux\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+0] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")
    print("\033[1;38;2;160;140;180m To go back type \033[4;38;2;190;180;200mback\033[0;37m")

def termux_submenu_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    table = PrettyTable()
    data = [[NameCol + "Download repositories", CommandCol + "repos", InfoCol + "Installs root and x11 repository" + TableCol],
            [NameCol + "Setup storage", CommandCol + "storage", InfoCol + "Setups termux storage" + TableCol],
            [NameCol + "Kali Nethunter", CommandCol + "kali", InfoCol + "Installs kali nethunter (rootless)" + TableCol],
            [NameCol + "THC-Hydra", CommandCol + "thchydra", InfoCol + "Installs thc-hydra !(not working now)!" + TableCol],]
    table.field_names = ["+", "\033[4;37mTermux\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+0] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")
    print("\033[1;38;2;160;140;180m To go back type \033[4;38;2;190;180;200mback\033[0;37m")

def hashing_submenu_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    table = PrettyTable()
    data = [[NameCol + "MD5", CommandCol + "md5", InfoCol + "Encodes string to md5" + TableCol],
            [NameCol + "SHA1", CommandCol + "sha1", InfoCol + "Encodes string to sha1" + TableCol],
            [NameCol + "SHA224", CommandCol + "sha224", InfoCol + "Encodes string to sha224" + TableCol],
            [NameCol + "SHA256", CommandCol + "sha256", InfoCol + "Encodes string to sha256" + TableCol],
            [NameCol + "SHA384", CommandCol + "sha384", InfoCol + "Encodes string to sha384" + TableCol],
            [NameCol + "SHA512", CommandCol + "sha512", InfoCol + "Encodes string to sha512" + TableCol],]
    table.field_names = ["+", "\033[4;37mHashing\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+0] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")
    print("\033[1;38;2;160;140;180m To go back type \033[4;38;2;190;180;200mback\033[0;37m")

def wlists_submenu_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    table = PrettyTable()
    data = [[NameCol + "Rock you", CommandCol + "rockyou", InfoCol + "Downloads rockyou wordlist", "\033[1;32m150 mb" + TableCol],
            [NameCol + "Small Wordlist", CommandCol + "small", InfoCol + "Downloads small wordlist", "\033[1;32m340 mb" + TableCol],
            [NameCol + "Big Wordlist", CommandCol + "big", InfoCol + "Downloads big wordlist", "\033[1;91m20 gb" + TableCol],
            [NameCol + "Bigone2016", CommandCol + "bigone", InfoCol + "Downloads Bigone2016 wordlist", "\033[1;32m513 mb" + TableCol],
            [NameCol + "Crackdown2016", CommandCol + "crackdown", InfoCol + "Downloads Crackdown2016 wordlist", "\033[1;32m705 mb" + TableCol],
            [NameCol + "Insider2016", CommandCol + "insider", InfoCol + "Downloads Insider2016 wordlist", "\033[1;32m116 mb" + TableCol],
            [NameCol + "Major2016", CommandCol + "major", InfoCol + "Downloads Major2016 wordlist", "\033[1;91m1,1 gb" + TableCol],
            [NameCol + "Neo2016", CommandCol + "neo", InfoCol + "Downloads Neo2016 wordlist", "\033[1;32m920 mb" + TableCol],
            [NameCol + "Potential2016", CommandCol + "potential", InfoCol + "Downloads Potential2016 wordlist", "\033[1;32m174 mb" + TableCol],
            [NameCol + "Ransom2016", CommandCol + "ransom", InfoCol + "Downloads Ransom2016 wordlist", "\033[1;32m295 mb" + TableCol],]
    table.field_names = ["+", "\033[4;37mWordlists\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?\033[0;30m", "\033[4;38;2;100;100;180mSize" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+0] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")
    print("\033[1;38;2;160;140;180m To go back type \033[4;38;2;190;180;200mback\033[0;37m")

def windows_powerplan_submenu_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    UlPlan = "\033[1;92mEnabled\033[0;37m" if os.path.exists("misc/windows/PP/ultimate.txt") else "\033[1;91mDisabled\033[0;37m"
    BlPlan = "\033[1;92mEnabled\033[0;37m" if os.path.exists("misc/windows/PP/balanced.txt") else "\033[1;91mDisabled\033[0;37m"
    PSPlan = "\033[1;92mEnabled\033[0;37m" if os.path.exists("misc/windows/PP/saver.txt") else "\033[1;91mDisabled\033[0;37m"

    table = PrettyTable()
    data = [[NameCol + "Ultimate", f"{UlPlan}", CommandCol + "ultimate", InfoCol + "Enables/Disables ultimate power plan on your pc" + TableCol],
        [NameCol + "Balanced", f"{BlPlan}", CommandCol + "balanced", InfoCol + "Enables/Disables balanced power plan on your pc" + TableCol],
        [NameCol + "Power saver", f"{PSPlan}", CommandCol + "saver", InfoCol + "Enables/Disables power saver power plan on your pc" + TableCol],]
    table.field_names = ["+", "\033[4;37mPower Plans\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m", "\033[4;38;2;160;180;244mStatus\033[0;37m","\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+0] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")
    print("\033[1;38;2;160;140;180m To go back type \033[4;38;2;190;180;200mback\033[0;37m")

def windows_software_submenu_manual():
    NameCol = '\033[1;93m'
    CommandCol = '\033[0;38;2;200;200;200m'
    InfoCol = '\033[1;90m'
    TableCol = "\033[0;38;2;50;50;50m"

    # Checks
    PuttyE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/putty.exe") else "\033[1;91mX\033[0;37m"
    WinscpE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/WinSCP.exe") else "\033[1;91mX\033[0;37m"
    ProcE = "\033[1;92mX\033[0;37m" if os.path.exists("./misc/windows/Programs/ProcHacker/x64/ProcessHacker.exe") or os.path.exists("./misc/windows/Programs/ProcHacker/x86/ProcessHacker.exe") else "\033[1;91mX\033[0;37m"
    WinaeroE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/WinaeroTweaker.exe") else "\033[1;91mX\033[0;37m"
    lastE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/LastActivityView.exe") else "\033[1;91mX\033[0;37m"
    WiztreeE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/WizTree") else "\033[1;91mX\033[0;37m"
    untoolE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/UninstallTool") else "\033[1;91mX\033[0;37m"
    hxdE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/HxD.exe") else "\033[1;91mX\033[0;37m"
    vlcE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/VLC.exe") else "\033[1;91mX\033[0;37m"
    obsE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/OBS.exe") else "\033[1;91mX\033[0;37m"
    audaE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/audacity.exe") else "\033[1;91mX\033[0;37m"
    islcE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/ISLC.exe") else "\033[1;91mX\033[0;37m"
    hwE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/HWinfo/")else "\033[1;91mX\033[0;37m"
    sandE = "\033[1;92mX\033[0;37m" if os.path.exists("./misc/windows/Programs/Sandboxie/Sandboxie_x64.exe") or os.path.exists("./misc/windows/Programs/Sandboxie/Sandboxie_x86.exe") else "\033[1;91mX\033[0;37m"
    HandE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/HandBrake.exe") else "\033[1;91mX\033[0;37m"
    WinE = "\033[1;92mX\033[0;37m" if os.path.exists("./misc/windows/Programs/Winrar/winrar_x64.exe") or os.path.exists("./misc/windows/Programs/Winrar/winrar_x86.exe") else "\033[1;91mX\033[0;37m"
    z7E = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/7z.exe") else "\033[1;91mX\033[0;37m"
    rufE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/rufus.exe") else "\033[1;91mX\033[0;37m"
    balE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/etcher.exe") else "\033[1;91mX\033[0;37m"
    ghidraE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/Ghidra/ghidraRun.bat") else "\033[1;91mX\033[0;37m"
    x64dbgE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/x64dbg/x96dbg.exe") else "\033[1;91mX\033[0;37m"
    vboxE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/Vbox.exe") else "\033[1;91mX\033[0;37m"
    vmwE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/VMware.exe") else "\033[1;91mX\033[0;37m"
    hashE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/hashcat/hashcat.exe") else "\033[1;91mX\033[0;37m"
    wireE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/Wireshark/WiresharkPortable64.exe") else "\033[1;91mX\033[0;37m"
    codE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/VSCodium.exe") else "\033[1;91mX\033[0;37m"
    nmapE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/nmap.exe") else "\033[1;91mX\033[0;37m"
    dieE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/DIE/die.exe") else "\033[1;91mX\033[0;37m"
    peidE = "\033[1;92mX\033[0;37m" if os.path.exists("misc/windows/Programs/peid/PEiD.exe") else "\033[1;91mX\033[0;37m"

    table = PrettyTable()
    data = [[NameCol + "Putty", "\033[1;38;2;180;127;0mP",f"{PuttyE}", CommandCol + "putty", InfoCol + "You can easily connect to servers" + TableCol],
            [NameCol + "WinSCP", "\033[1;38;2;180;127;0mP",f"{WinscpE}", CommandCol + "winscp", InfoCol + "You can easily send files to your server" + TableCol],
            [NameCol + "Process Hacker", "\033[1;38;2;180;127;0mP",f"{ProcE}", CommandCol + "proc", InfoCol + "Better task manager" + TableCol],
            [NameCol + "Winaero Tweaker", "\033[1;96mI",f"{WinaeroE}", CommandCol + "winaero", InfoCol + "Some tweaks for windows" + TableCol],
            [NameCol + "Last Activity View", "\033[1;38;2;180;127;0mP",f"{lastE}", CommandCol + "last", InfoCol + "Shows when certain tasks were started" + TableCol],
            [NameCol + "WizTree", "\033[1;38;2;180;127;0mP",f"{WiztreeE}", CommandCol + "wiztree", InfoCol + "Shows what you have in your drive" + TableCol],
            [NameCol + "Uninstall Tool", "\033[1;38;2;180;127;0mP",f"{untoolE}", CommandCol + "untool", InfoCol + "Can uninstall software from your pc" + TableCol],
            [NameCol + "HxD Editor", "\033[1;38;2;180;127;0mP",f"{hxdE}", CommandCol + "hxd", InfoCol + "You can edit hex values of files" + TableCol],
            [NameCol + "VLC", "\033[1;96mI",f"{vlcE}", CommandCol + "vlc", InfoCol + "Media player for windows" + TableCol],
            [NameCol + "OBS", "\033[1;96mI",f"{obsE}", CommandCol + "obs", InfoCol + "You can record your screen with this" + TableCol],
            [NameCol + "Audacity", "\033[1;96mI",f"{audaE}", CommandCol + "audacity", InfoCol + "You can record your voice" + TableCol],
            [NameCol + "ISLC", "\033[1;96mI",f"{islcE}", CommandCol + "islc", InfoCol + "Fixes standby memory (RAM)" + TableCol],
            [NameCol + "HW Info", "\033[1;38;2;180;127;0mP",f"{hwE}", CommandCol + "hwinf", InfoCol + "Shows temps, voltage and more of your components" + TableCol],
            [NameCol + "Sanboxie", "\033[1;96mI",f"{sandE}", CommandCol + "sanboxie", InfoCol + "Creates sort of vm where you can run malicious software" + TableCol],
            [NameCol + "Handbrake", "\033[1;96mI",f"{HandE}", CommandCol + "handbrake", InfoCol + "You can make smaller video files and lot more" + TableCol],
            [NameCol + "Winrar", "\033[1;96mI",f"{WinE}", CommandCol + "winrar", InfoCol + "Best tool for unzipping archives" + TableCol],
            [NameCol + "7 Zip", "\033[1;96mI",f"{z7E}", CommandCol + "7zip", InfoCol + "Good tool for unzipping archives" + TableCol],
            [NameCol + "Rufus", "\033[1;38;2;180;127;0mP",f"{rufE}", CommandCol + "rufus", InfoCol + "You can flash OS on usb stick" + TableCol],
            [NameCol + "Etcher", "\033[1;38;2;180;127;0mP",f"{balE}", CommandCol + "etcher", InfoCol + "You can flash OS on usb stick, or clone it" + TableCol],
            [NameCol + "Ghidra", "\033[1;38;2;180;127;0mP",f"{ghidraE}", CommandCol + "ghidra", InfoCol + "Program decompiler/debugger" + TableCol],
            [NameCol + "x64dbg", "\033[1;38;2;180;127;0mP",f"{x64dbgE}", CommandCol + "x64dbg", InfoCol + "Program decompiler/debugger" + TableCol],
            [NameCol + "Virtual box", "\033[1;96mI",f"{vboxE}", CommandCol + "vbox", InfoCol + "Virtualization software" + TableCol],
            [NameCol + "VMware", "\033[1;96mI",f"{vmwE}", CommandCol + "vmw", InfoCol + "Virtualization software" + TableCol],
            [NameCol + "Hashcat", "\033[1;38;2;180;127;0mP",f"{hashE}", CommandCol + "hash", InfoCol + "Hash cracking software" + TableCol],
            [NameCol + "Wireshark", "\033[1;38;2;180;127;0mP",f"{wireE}", CommandCol + "wire", InfoCol + "Traffic sniffer" + TableCol],
            [NameCol + "VScodium", "\033[1;96mI",f"{codE}", CommandCol + "codium", InfoCol + "VS code, but without microsofts BS" + TableCol],
            [NameCol + "Nmap", "\033[1;96mI",f"{nmapE}", CommandCol + "nmap", InfoCol + "Port scanner" + TableCol],
            [NameCol + "DIE", "\033[1;38;2;180;127;0mP",f"{dieE}", CommandCol + "die", InfoCol + "File analyzer" + TableCol],
            [NameCol + "Peid", "\033[1;38;2;180;127;0mP",f"{peidE}", CommandCol + "peid", InfoCol + "File analyzer" + TableCol],
            ]
    table.field_names = ["+", "\033[4;37mUseful Software\033[0;37m \033[4;38;2;170;190;254mOptions\033[0;30m", "\033[4;38;2;140;160;224mType\033[0;37m", "\033[4;38;2;160;180;244mStatus\033[0;37m", "\033[4;38;2;150;170;234mCommand\033[0;30m","\033[4;38;2;130;150;214mWhat is it?" + TableCol]
    table.align = "l"
    for i, row in enumerate(data):
        table.add_row([i+0] + row)
    table = str(table).strip("|+-").replace("|", " ").replace("+", " ")
    print(table + "\033[1;37m")
    print("\033[1;38;2;160;140;180m To go back type \033[4;38;2;190;180;200mback\033[0;37m")
############################################################################################################
######################################## Skajp TLS main menu ###############################################
############################################################################################################

def Credits():
    print("\n\033[1;93m Credits of Skajp TLS")
    print("\n\033[1;93m Creator \033[1;90m> \033[1;37mSkajp")
    print("\n\033[1;90m This is multi tool with few scripts made in python")
    print("\033[1;90m There will be a lot of other things in this tool in future")
    print("\033[1;90m You can use some commands that are avaible in normal cmd in windows or terminal in linux (kali)")

def CheckForUpdates():
    f=False
    try:
        if os.name == 'nt':
            try: subprocess.check_output("ping 1.1.1.1 -n 1", shell=True);f=True
            except: f=False
            try: subprocess.check_output("ping 8.8.8.8 -n 1", shell=True);f=True
            except: f=False
        else:
            try: subprocess.check_output("ping -c 1 1.1.1.1", shell=True, stderr=subprocess.STDOUT);f=True
            except: f=False
            try: subprocess.check_output("ping -c 1 8.8.8.8", shell=True, stderr=subprocess.STDOUT);f=True
            except: f=False
        if f: 
            response = requests.get('https://pastebin.com/raw/Y4fBQP1h')
            if int(tlsver) == int(response.text): print('\033[1;32m' + "\n Up to date")
            elif int(tlsver) > int(response.text): print('\033[1;34m' + "\n Newer (testing)")
            else: print('\033[1;31m' + "\n Old")
        else: print('\033[1;31m' + "\n No internet connection\n Some features may not work properly"); time.sleep(2)
    except: print('\033[1;31m' + "\n No internet connection\n Some features may not work properly"); time.sleep(2)


def InChck():
    f=False
    if os.name=='nt':
        try: subprocess.check_output("ping 1.1.1.1 -n 1", shell=True);f=True
        except: f=False
        try: subprocess.check_output("ping 8.8.8.8 -n 1", shell=True);f=True
        except: f=False
    else:
        try: subprocess.check_output("ping -c 1 1.1.1.1", shell=True, stderr=subprocess.STDOUT);f=True
        except: f=False
        try: subprocess.check_output("ping -c 1 8.8.8.8", shell=True, stderr=subprocess.STDOUT);f=True
        except: f=False
    if not f:return True if input("\n\033[1;37m  No internet connection detected, would you want to bypass it? \033[0;90m(Y/N)\033[1;37m ").lower() == "y" else False
    else: return True

def LoadSettings(thing):
    SettingsJsonFile = open("./misc/settings/settings.json")
    SettingsJson = json.load(SettingsJsonFile)
    logo_type = SettingsJson["logo_type"]
    r = SettingsJson["static-colors"]["r"]
    g = SettingsJson["static-colors"]["g"]
    b = SettingsJson["static-colors"]["b"]
    SettingsJsonFile.close()
    if thing == "logo_type": return logo_type
    elif thing == "cols": return r,g,b

def logo():
    clear()
    sys.stdout.write("\x1b]2;Skajp TLS\x07")
    logo_type = LoadSettings("logo_type")
    if logo_type == "random": logo_col1 = random.randrange(random.randrange(60), 255); logo_col2 = random.randrange(random.randrange(60), 255); logo_col3 = random.randrange(random.randrange(60), 255)
    if logo_type == "static": cR, cG, cB = LoadSettings("cols"); logo_col1 = int(cR); logo_col2 = int(cG); logo_col3 = int(cB)
    print(f"""\033[1;38;2;{logo_col1};{logo_col2};{logo_col3}m
       _____ __           _          ________   _____
      / ___// /______ _  (_)___     /_  __/ /  / ___/
      \__ \/ //_/ __ `/ / / __ \     / / / /   \__ \ 
     ___/ / ,< / /_/ / / / /_/ /    / / / /______/ / 
    /____/_/|_|\__,_/_/ / .___/    /_/ /_____/____/  
                   /___/_/                          
                                \033[1;90mBy Skajp
    """)
    print(f"\033[1;90m Version: {tlsver}")
    print(f"\033[1;90m Type 'help' or '?' to show help menu")
    menu()

def menu():
    while True:
        cho = input("\n \033[1m\033[4;37mskajptls\033[0m \033[1;31mNT \033[1;90m> \033[0;37m").lower() if os.name == 'nt' else input("\n \033[1m\033[4;37mskajptls\033[0m \033[1;90m> \033[0;37m").lower() 
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        # options
        if cho in ['r']: clear(); logo()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['clear', 'cls']: clear()
        elif cho in ['credits', 'cred']: Credits()
        elif cho in ['settings','set']: Settings_menu()
        # Manuals
        elif cho in ['help', '?', '??']: help_manual()
        elif cho in ['opt', 'options']: options_manual()
        # Imported modules from ./misc/modules/
        elif cho in ['pscan', '0']: pscan.main() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['geoip','iplookup', '1']: iplookup.IPLookUp() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['mac','maclookup', '2']: maclookup.MacAddrLookUp() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['myip', '3']: getip.myip() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['aftp', '4']: anonftp.FTPanonLOG() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['mailscraper', '5']: mailscrape.EmailScrape() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['proxies', '6']: proxyscrape.scrapes() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['chat', '7']: chat_submenu() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['zipcrack', '8']: zipcrack.ZipCracking() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['pyobs', '9']: obs.Obs()
        elif cho in ['keylog', '10']: keylogger.Keylogger() if InChck() else print("\033[1;31m\n No internet connection")
        # Functions from this file
        # Submenus
        elif cho in ['windows', 'win','11']: windows_submenu() if os.name == 'nt' else print('\033[1;31m' + "\n You need windows to use this")
        elif cho in ['linux', 'kali', 'kalilinux','12']: kalilinux_submenu() if os.name == 'posix' and os.path.exists("/boot/grub/themes/kali/") else print('\033[1;31m' + "\n You need linux to use this")
        elif cho in ['termux','13']: termux_submenu() if os.name == 'posix' and os.path.exists("/data/data/com.termux") else print('\033[1;31m' + "\n You need termux to use this")
        elif cho in ['webs', 'web','14']: webs_submenu() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['hash', 'hashes', 'hashing','15']: hash_submenu()
        elif cho in ['wlists', 'wordlists','16']: print("Working on") #Wlist_submenu() if InChck() else print("\033[1;31m\n No internet connection")
        # Commands that can be run from tool
        else:
            if os.name == 'nt':
                winc = ["ipconfig","dir","echo","ping","whoami","cd","start"]
                try:
                    if cho in winc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")
            else:
                lc = ["searchsploit","ifconfig","msfconsole","nmap","ls","cd","cat","sudo","apt","echo","ping","whoami","uname","mdkir","rm","pwd","touch","nano","vim","service","systemctl","ip"]
                try:
                    if cho in lc: print(); os.system(fullcho)
                    else: 
                        if len(cho) < 1: pass
                        else: print('\033[1;31m' + "\n Unknown Command")
                except: 
                    print('\033[1;31m' + "\n Unknown Command")



##########################################################################################
if os.name == 'posix' or 'Darwin':FNULL = open(os.devnull, 'w')


if os.path.exists('./misc/.ver'):
    if os.path.exists("./misc/proxies.txt"):
        clear()
        import sys, random, time, subprocess, threading, concurrent.futures, requests, datetime, base64, codecs, string, json, socket, requests.exceptions, urllib.parse, re, webbrowser, platform, shutil
        from bs4 import BeautifulSoup
        from collections import deque
        from async_timeout import timeout
        from prettytable import PrettyTable
        tlsver = 1;CheckForUpdates(); logo(); menu()
    else:
        import subprocess
        clear()
        try:
            with open("requirements.txt") as f:
                lol = []; count = 1; finalol = []
                for i in f.readlines(): lol.append(i)
                lenghtoffile = sum(1 for line in open('requirements.txt'))
                for i in lol:
                    if count == int(lenghtoffile): finalol.append(i)
                    else: finalol.append(i[:-1])
                    count += 1
        except:
            clear()
            print("\n\033[1;91m Failed to locate 'requirements.txt' folder")
            time.sleep(5)
            quit()
        for i in finalol:
            print("\n")
            print(f"\033[1;93m Installing \033[1;90m> \033[0;37m{i}", end="\r")
            PIPver = ""
            for a in str(subprocess.check_output("pip --version", shell=True, stderr=subprocess.STDOUT)).split(" ")[1]:
                if a in ["1","2","3","4","5","6","7","8","9","0"]:
                    PIPver += a
                    if len(PIPver) < 4:PIPver += "0"
            subprocess.call(f"pip install {i} >nul", shell=True, stdout=FNULL, stderr=subprocess.STDOUT) if os.name == 'nt' else subprocess.call(f"pip install {i} --break-system-package", shell=True, stdout=FNULL, stderr=subprocess.STDOUT) if int(PIPver) >= 2300 else subprocess.call(f"pip install {i}", shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
            print(f"\033[1;92m Installed \033[1;90m> \033[0;37m{i}  ", end="\r")
        os.mkdir('./misc/chats')
        os.mkdir('./misc/keylogger')
        os.mkdir('./misc/keylogger/clients')
        os.mkdir('./misc/keylogger/logs')
        os.mkdir('./misc/mails')  
        os.mkdir('./misc/CrackedZips') 
        os.mkdir('./misc/wordlists') 
        os.mkdir('./misc/windows') 
        os.mkdir('./misc/windows/PP') 
        os.mkdir('./misc/windows/Programs') 
        os.mkdir('./misc/AnonFiles')
        open('./misc/proxies.txt', 'x')
        import sys, random, time, subprocess, threading, concurrent.futures, requests, datetime, base64, codecs, string, json, socket, requests.exceptions, urllib.parse, re, webbrowser, platform, shutil
        from bs4 import BeautifulSoup
        from collections import deque
        from async_timeout import timeout
        from prettytable import PrettyTable
        tlsver = 1; CheckForUpdates(); logo(); menu()
else:
    import subprocess
    open('./misc/.ver', 'x')
    clear()
    try:
        with open("requirements.txt") as f:
            lol = []; count = 1; finalol = []
            for i in f.readlines(): lol.append(i)
            lenghtoffile = sum(1 for line in open('requirements.txt'))
            for i in lol:
                if count == int(lenghtoffile): finalol.append(i)
                else: finalol.append(i[:-1])
                count += 1
    except:
        clear()
        print("\n\033[1;91m Failed to locate 'requirements.txt' folder")
        time.sleep(5)
        quit()
    for i in finalol:
        print("\n")
        print(f"\033[1;93m Installing \033[1;90m> \033[0;37m{i}", end="\r")
        PIPver = ""
        for a in str(subprocess.check_output("pip --version", shell=True, stderr=subprocess.STDOUT)).split(" ")[1]:
            if a in ["1","2","3","4","5","6","7","8","9","0"]:
                PIPver += a
                if len(PIPver) < 4:PIPver += "0"
        subprocess.call(f"pip install {i}", shell=True, stdout=FNULL, stderr=subprocess.STDOUT) if os.name == 'nt' else subprocess.call(f"pip install {i} --break-system-package", shell=True, stdout=FNULL, stderr=subprocess.STDOUT) if int(PIPver) >= 2300 else subprocess.call(f"pip install {i}", shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        print(f"\033[1;92m Installed \033[1;90m> \033[0;37m{i}  ", end="\r")
    os.mkdir('./misc/chats')
    os.mkdir('./misc/keylogger')
    os.mkdir('./misc/keylogger/clients')
    os.mkdir('./misc/keylogger/logs')
    os.mkdir('./misc/mails') 
    os.mkdir('./misc/CrackedZips') 
    os.mkdir('./misc/wordlists') 
    os.mkdir('./misc/windows') 
    os.mkdir('./misc/windows/PP') 
    os.mkdir('./misc/windows/Programs')
    os.mkdir('./misc/AnonFiles')
    open('./misc/proxies.txt', 'x')
    import sys, random, time, subprocess, threading, concurrent.futures, requests, datetime, base64, codecs, string, json, socket, requests.exceptions, urllib.parse, re, webbrowser, platform, shutil
    from bs4 import BeautifulSoup
    from collections import deque
    from async_timeout import timeout
    from prettytable import PrettyTable
    tlsver = 1;CheckForUpdates(); logo(); menu()