
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
import os, time, sys, subprocess

__version__ = 1

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

def clear():os.system('cls' if os.name == 'nt' else 'clear')
if os.name == 'posix':FNULL=open(os.devnull, 'w')

# Import Modules Made By Skajp
if os.path.exists("./misc"): from misc.modules import pscan, iplookup, mailscrape, obs, getip, OnlineChat, keylogger, anonftp, maclookup, hashes, changemac
else:
    clear()
    print(f"\n{bad} Failed to locate './misc' folder")
    time.sleep(5)
    quit()

def ResetTool():
    print()
    p = '.'
    for i in range(3):
        print('\033[1;31m' + f" Reseting Skajp TLS{p}", end="\r")
        p += '.'
        time.sleep(0.3)
    os.remove("misc/.a")
    shutil.rmtree("misc/chats")
    shutil.rmtree("misc/keylogger/")
    shutil.rmtree("misc/mails")
    shutil.rmtree("misc/wordlists")
    shutil.rmtree("misc/modules/__pycache__")
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


 ##########################################################################
def PrintTable(nums,values,t):
  ColOfNames = "\033[3;38;2;170;190;254m"
  NameCol = '\033[1;93m'
  CommandCol = '\033[0;38;2;200;200;200m'
  InfoCol = '\033[1;90m'
  TableCol = "\033[0;38;2;50;50;50m"
  if t:
    values.append(["Options","Commands","Description"])
    if nums:
      counter = 0
      a = 1
      lI, lJ, lK = 0, 0, 0
      for i,j,k in values:
        if int(len(i))>lI:lI=len(i)
        if int(len(j))>lJ:lJ=len(j)
        if int(len(k))>lK:lK=len(k)
      if len(values) >= 10: a = 2
      if len(values) >= 100: a = 3
      print(f"\n{' '*int(a+2)}  {ColOfNames}{f'Options':<{int(lI+1)}}{white}  {ColOfNames}{'Commands':<{int(lJ+1)}}{white}  {ColOfNames}{'Description':<{int(lK+1)}}{white}")
      print(f"{TableCol}{'-'*int(a+2)} {'-'*int(lI+1)}- -{'-'*int(lJ+1)} -{'-'*int(lK+1)}{white}")
      values.pop(len(values)-1)
      for i,j,k in values: 
        if a == 1:
          SubTra = 0 
          print(f' {TableCol}{" "*SubTra}{counter}   {NameCol}{i:<{int(lI+1)}}  {CommandCol}{j:<{int(lJ+1)}}  {InfoCol}{k:<{int(lK+1)}}')
          counter += 1
        elif a == 2:
          SubTra = 1 if counter < 10 else -1 
          print(f' {TableCol}{" "*SubTra}{counter}   {NameCol}{i:<{int(lI+1)}}  {CommandCol}{j:<{int(lJ+1)}}  {InfoCol}{k:<{int(lK+1)}}')
          counter += 1
        elif a == 3:
          SubTra = 2 if counter < 10 else 1 if counter < 100 else -1
          print(f' {TableCol}{" "*SubTra}{counter}   {NameCol}{i:<{int(lI+1)}}  {CommandCol}{j:<{int(lJ+1)}}  {InfoCol}{k:<{int(lK+1)}}')
          counter += 1
    if not nums:
      lI, lJ, lK = 0, 0, 0
      for i,j,k in values:
        if int(len(i))>lI:lI=len(i)
        if int(len(j))>lJ:lJ=len(j)
        if int(len(k))>lK:lK=len(k)
      print(f"\n     {f'{ColOfNames}Options{white}':<{int(lI+1)}}    {f'{ColOfNames}Commands{white}':<{int(lJ+1)}}   {f'{ColOfNames}Description{white}':<{int(lK+1)}}")
      print(f"{TableCol}--- {'-'*int(lI+1)}- -{'-'*int(lJ+1)} -{'-'*int(lK+1)}{white}")
      values.pop(len(values)-1)
      for i,j,k in values: 
        print(f' {TableCol}x   {NameCol}{i:<{int(lI+1)}}  {CommandCol}{j:<{int(lJ+1)}}  {InfoCol}{k:<{int(lK+1)}}')
  else:
    values.append(["Options","Status","Commands","Description"])
    if nums:
      counter = 0
      a = 1
      lI, lJ, lK, lH = 0, 0, 0, 0
      for i,j,k,h in values:
        if int(len(i))>lI:lI=len(i)
        if int(len(j))>lJ:lJ=len(j)
        if int(len(k))>lK:lK=len(k)
        if int(len(h))>lH:lH=len(h)
      if len(values) >= 10: a = 2
      if len(values) >= 100: a = 3
      print(f"\n{' '*int(a+2)}  {ColOfNames}{f'Options':<{int(lI+1)}}{white}  {ColOfNames}{'Status':<{int(lJ+1)}}{white}  {ColOfNames}{'Commands':<{int(lK+1)}}{white}  {ColOfNames}{'Description':<{int(lH+1)}}{white}")
      print(f"{TableCol}{'-'*int(a+2)} {'-'*int(lI+1)}- {'-'*int(lJ+1)}- -{'-'*int(lK+1)} -{'-'*int(lH+1)}{white}")
      values.pop(len(values)-1)
      for i,j,k,h in values:
        if j in ["static","random"]:ColIDK = "\033[1;92m" if j == "static" else "\033[1;96m"
      for i,j,k,h in values: 
        if a == 1:
          SubTra = 0 
          print(f' {TableCol}{" "*SubTra}{counter}   {NameCol}{i:<{int(lI+1)}}  {ColIDK}{j:<{int(lJ+1)}}  {CommandCol}{k:<{int(lK+1)}}  {InfoCol}{h:<{int(lH+1)}}')
          counter += 1
        elif a == 2:
          SubTra = 1 if counter < 10 else -1 
          print(f' {TableCol}{" "*SubTra}{counter}   {NameCol}{i:<{int(lI+1)}}  {ColIDK}{j:<{int(lJ+1)}}  {CommandCol}{k:<{int(lK+1)}}  {InfoCol}{h:<{int(lH+1)}}')
          counter += 1
        elif a == 3:
          SubTra = 2 if counter < 10 else 1 if counter < 100 else -1
          print(f' {TableCol}{" "*SubTra}{counter}   {NameCol}{i:<{int(lI+1)}}  {ColIDK}{j:<{int(lJ+1)}}  {CommandCol}{k:<{int(lK+1)}}  {InfoCol}{h:<{int(lH+1)}}')
          counter += 1
    if not nums:
      lI, lJ, lK, lH = 0, 0, 0, 0
      for i,j,k,h in values:
        if int(len(i))>lI:lI=len(i)
        if int(len(j))>lJ:lJ=len(j)
        if int(len(k))>lK:lK=len(k)
        if int(len(h))>lH:lH=len(h)
      print(f"\n     {f'{ColOfNames}Options{white}':<{int(lI+1)}}         {f'{ColOfNames}Status{white}':<{int(lJ+1)}}   {f'{ColOfNames}Commands{white}':<{int(lK+1)}}   {f'{ColOfNames}Description{white}':<{int(lH+1)}}")
      print(f"{TableCol}--- {'-'*int(lI+1)}- {'-'*int(lJ+1)}- -{'-'*int(lK+1)} -{'-'*int(lH+1)}{white}")
      values.pop(len(values)-1)
      for i,j,k,h in values: 
        print(f' {TableCol}x   {NameCol}{i:<{int(lI+1)}}  {CommandCol}{j:<{int(lJ+1)}}  {CommandCol}{k:<{int(lK+1)}}  {InfoCol}{h:<{int(lH+1)}}')

def help_manual():
  values = [
    ["Options",   "opt",      "Shows every option of skajp tools"],
    ["Settings",  "settings", "Shows settings of skajp tools"],
    ["Help",      "help",     "Shows this menu"],
    ["Execute",   "exe",      "Execute commands in terminal"],
    ["Clear",     "cls",      "Clears terminal"],
    ["Exit",      "exit",     "Exits tool "]]
  PrintTable(False,values,True)

def helpsub_manual():
  values = [
    ["Options",   "opt",      "Shows every option of skajp tools"],
    ["Settings",  "settings", "Shows settings of skajp tools"],
    ["Help",      "help",     "Shows this menu"],
    ["Execute",   "exe",      "Execute commands in terminal"],
    ["Clear",     "cls",      "Clears terminal"],
    ["Back",      "back",     "Goes back"],
    ["Exit",      "exit",     "Exits tool "]]
  PrintTable(False,values,True)

def options_manual():
  values = [
    ["Port Scanner", "pscan", "Just basic port scanner"],
    ["IP Look Up", "iplook", "Basic ip look up"],
    ["Mac Look Up", "macl", "Basic mac address look up"],
    ["Your IPs", "myip", "Shows you your local and public ip"],
    ["Anonymous FTP", "aftp", "Tests anonymous login on FTP"],
    ["Mail scraper", "mailscrape", "Scrapes mails from websites"],
    ["Online Chat", "chat", "Creates chat where you can chat with friends"],
    ["Python Obfuscator", "pyobs", "Obfuscates python code"],
    ["Keylogger", "keylog", "Simple keylogger"],
    ["Change Mac", "chmac", "Changes your mac address"],
    ["Webs", "webs", "Webs submenu"],
    ["Hashing", "hash", "Hashing submenu"],
    ["Mac submenu", "mac", "Changing mac address"]
  ]
  PrintTable(True,values,True)

def webs_manual():
  values = [
    ["Fake Name Generator",    "fakename",      "Generates random person info"],
    ["Vedbex",                 "vedbex",        "Multi tool in web"],
    ["ASCII Art",              "ascii",         "Opens 2 sites with ASCII art"],
    ["Fancy Fonts",            "fonts",         "You can make fancy font here"],
    ["Bugcrowd",               "bugcrowd",      "You can get money from finding bugs in webs"],
    ["Malware Database",       "malwaredb",     "Github repo with some malwares"],
    ["Tineye",                 "tineye",        "Image analyzer"],
    ["haveibeenpwned",         "pwned",         "Tells you if you are in some leaked db"],
    ["Python Obsfucator",      "pyobs",         "Obsfucates python code"],
    ["Password Possibilities", "passposs",      "Calculates how many possible can be with custom parameters"],
    ["Lullar",                 "lullar",        "OSINT tool"],
    ["Virustotal",             "virustotal",    "Examines file with vms and avs"],
    ["Metadata Reader",        "metaread",      "Reads metadata from file"],
    ["Python 2 To 3 Convertor","py2to3",        "Converts python 2 code to python 3 code"],
    ["Cookie Convertor",       "cookieconv",    "Converts netscape cookie to json cookie"],
    ["Portable Apps",          "portapps",      "You can download some portable apps"],
    ["Photosherlock",          "photosherlock", "Another image analyzer"],
    ["Etools",                 "etools",        "Multi tool in web"],
    ["Webarchive",             "webarchive",    "You can find some archived webs on there"],
    ["Stackoverflow",          "stackoverflow", "Biggest forum for programers"],
    ["Deepl Translator",       "deepl",         "Something like google translator"],
    ["Cloud Convert",          "cloudconv",     "You can convert file to other format"],
    ["Canary Tokens",          "canarytokens",  "You can create file with ip grabber"],
    ["Pimeyes",                "pimeyes",       "Another image analyzer"],
    ["InsecCam",               "inseccam",      "Shows cameras that are open to the web"],
    ["Keyboard Codes",         "keyboardcodes", "Can show you what code has key on keyboard"],
    ["Snapchat Map",           "snapmap",       "This site shows you snapchat map"],
    ["Shodan",                 "shodan",        "This site shows devices that have opened ports to the internet"],
    ["Temp Mail",              "tempmail",      "This site creates temp mail for random register"],
    ["Explain Shells",         "explainshell",  "This site will explain any shell command"],
    ["Bash Upload",            "bashupload",    "This site allows you to share files that have 50GB for 3 days"],
    ["Security.org",           "secpass",       "This site shows you how strong password you have"],
    ["Gtfobins",               "gtfobins",      "Some interessting commands for linux"],
    ["CyberChef",              "cyberchef",     "One of the best for encryption/decryption"],
    ["Recieve SMS",            "sms",           "You can recieve sms on anonymous number"],
    ["Spokeo",                 "spok",          "You can search for people here"],
    ["AnsiiToHex",             "ath",           "Some site for cryptography"],
    ["Aperisolve",             "aperi",         "This site allows you to do simple stego on images"],
    ["Dcode",                  "dcode",         "You can find lot of cypher, analyzers and more"],
    ["Pentestmonkey",          "penm",          "Some reverse shell commands"],
    ["Hash Identify",          "hashi",         "Identify almost any hash on this site"],
    ["Decode Hash",            "dechash",       "You can try decoding some hashes here"],
    ["Md5 Calc",               "m5calc",        "You can find some tools here"],
    ["Mail Spoofer",           "mailspoof",     "You can send spoofed emails"],
    ["Rockstar",               "rockstar",      "Lyrics can be translated to code"],
    ["Exifer",                 "exifer",        "Website for exif data"],
    ["Whocalld",               "wcalld",        "Some info about telephone number"],
    ["Intel Techniques",       "itech",         "Some nice tools for osint"],
    ["Crack Station",          "crack",         "Database of hashes"],
    ["Faceidcheck",            "facecheck",     "Analyzes faces"],
    ["Payload All Things",     "pat",           "Lot of payloads"],
    ["Check-host",             "checkh",        "IP resolver"],
    ["Censys",                 "censys",        "Find devices across the web"],
    ["Anon Box",               "abox",          "Temporary mail"]
  ]
  PrintTable(True,values,True)

def settings_manual():
  values = [
    ["Reset Skajp TLS",       "reset",  "Resets all things in this tool"],
    ["Test Internet",         "ping",   "Tests conectivity"],
    ["Check Updates",         "update", "Check updates for Skajp TLS"],
    ["Size of ./misc",        "msize",  "Shows you size in bytes of ./misc folder"],
    ["Change Color of Logo",  "colors", "Submenu for logo colors"]
  ]
  PrintTable(True,values,True)
def settingsColors_manual():
  PathToSettings = "./misc/settings/settings.json"

  with open(PathToSettings, 'r') as f:data = json.load(f)
  logo_type = str(data["logo_type"]).strip()
  
  values = [
    ["Logo Type", logo_type ,"ltype", "Changes logo type between static and random"],
    ["Change Colors", "" , "chcol", "Change static rgb values"]
  ]
  PrintTable(True,values,False)

def hashing_submenu_manual():
  values = [
    ["md5",     "md5",    "Creates md5 hash"],
    ["sha1",    "sha1",   "Creates sha1 hash"],
    ["sha224",  "sha224", "Creates sha224 hash"],
    ["sha256",  "sha256", "Creates sha256 hash"],
    ["sha384",  "sha384", "Creates sha384 hash"],
    ["sha512",  "sha512", "Creates sha512 hash"]
  ]
  PrintTable(True,values,True)

def mac_manual():
  values = [
    ["Random Mac", "random", "Changes your mac"],
    ["Reset Mac", "reset", "Resets your mac"]
  ]
  PrintTable(True,values,True)
 ##########################################################################

def ChangeMacSubmenu():
  while True:
    cho = input(f"\n \033[1m\033[4;37mskajptls{white} (\033[1;38;2;200;127;0mMac\033[0;37m) \033[1;31mNT {grey}> {white}").lower() if os.name == 'nt' else input(f"\n \033[1m\033[4;37mskajptls{white} (\033[1;38;2;200;127;0mMac\033[0;37m) {grey}> {white}").lower() 
    try: fullcho = cho; cho = cho.split()[0]
    except: pass
    # Misc Options
    if cho in ['clear', 'cls']: clear()
    elif cho in ['exit', 'quit', 'q']: quit()
    elif cho in ['back']: main()
    elif cho in ['help', '?', '??']: helpsub_manual()
    elif cho in ['opt', 'options']: mac_manual()
    elif cho in ["exec", "e"]: os.system(fullcho[5:]) if cho == "exec" else os.system(fullcho[2:])
    # Commands
    elif cho in ['random', '0']: changemac.main()
    elif cho in ['reset','1']: changemac.reset()
    else:print(f"\n{bad} Command not found")

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
        print(f"\n{good} Logo type changed from {yellow}{data['logo_type']}{white} to {yellow}{ltype}{white}")
        data['logo_type'] = ltype

        with open(PathToSettings, 'w') as f: json.dump(data, f)
        
    elif a == "colors":
        with open(PathToSettings, 'r') as f: data = json.load(f)
        r = data['static-colors']['r']
        g = data['static-colors']['g']
        b = data['static-colors']['b']

        print(f"\n \033[1;92m R\033[1;90m: \033[1;37m{r}")
        print(f" \033[1;91m G\033[1;90m: \033[1;37m{g}")
        print(f" \033[1;94m B\033[1;90m: \033[1;37m{b}")

        def NewVals():
          print("  \n\033[1;93m New values\033[1;90m:\n")
          r = input(f" \033[1;91m R\033[1;90m: \033[1;37m")
          g = input(f" \033[1;92m G\033[1;90m: \033[1;37m")
          b = input(f" \033[1;94m B\033[1;90m: \033[1;37m")

          return r, g, b
        
        r,g,b = NewVals()
        if r > 0 or r < 255: print(f"\n{bad} Invalid color for R");r,g,b = NewVals()
        if g > 0 or g < 255: print(f"\n{bad} Invalid color for G");r,g,b = NewVals()
        if b > 0 or b < 255: print(f"\n{bad} Invalid color for B");r,g,b = NewVals()

        data['static-colors']['r'] = r
        data['static-colors']['g'] = g
        data['static-colors']['b'] = b

        with open(PathToSettings, 'w') as f: json.dump(data, f)

def Settings_menu():
    while True:
        cho = input(f"\n \033[1m\033[4;37mskajptls{white} (\033[1;38;2;200;127;0mSettings\033[0;37m) \033[1;31mNT {grey}> {white}").lower() if os.name == 'nt' else input(f"\n \033[1m\033[4;37mskajptls{white} (\033[1;38;2;200;127;0mSettings\033[0;37m) {grey}> {white}").lower() 
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        # Misc Options
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: main()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['opt', 'options']: settings_manual()
        elif cho in ["exec", "e"]: os.system(fullcho[5:]) if cho == "exec" else os.system(fullcho[2:])
        # Commands
        elif cho in ['reset', '0']: ResetTool()
        elif cho in ['internet','ping', '1']: PingTesting()
        elif cho in ['updates','checkup','ups','update', '2']: CheckForUpdates()
        elif cho in ['msize', 'misc', 'miscsize', '3']: print(f"\n\033[1;93m Size of \033[1;37m./misc \033[0;90m> \033[1;37m{get_misc_size()}\033[1;90m bytes")
        elif cho in ['colors', '4']: SettingsColors_menu()
        else:print(f"\n{bad} Command not found")

def SettingsColors_menu():
    while True:
        cho = input(f"\n \033[1m\033[4;37mskajptls{white} (\033[1;38;2;200;127;0mSettings/Color\033[0;37m) \033[1;31mNT {grey}> {white}").lower() if os.name == 'nt' else input(f"\n \033[1m\033[4;37mskajptls{white} (\033[1;38;2;200;127;0mSettings/Color\033[0;37m) {grey}> {white}").lower() 
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        # Misc Options
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: Settings_menu()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['opt', 'options']: settingsColors_manual()
        elif cho in ["exec", "e"]: os.system(fullcho[5:]) if cho == "exec" else os.system(fullcho[2:])
        # Commands
        elif cho in ['ltype', '0']: ChangeLogoStyle("logo_type")
        elif cho in ['chcol', '1']: ChangeLogoStyle("colors")
        else:print(f"\n{bad} Command not found")

def hashing_submenu():
  while True:
        cho = input(f"\n \033[1m\033[4;37mskajptls{white} (\033[1;38;2;200;127;0mHashes\033[0;37m) \033[1;31mNT {grey}> {white}").lower() if os.name == 'nt' else input(f"\n \033[1m\033[4;37mskajptls{white} (\033[1;38;2;200;127;0mHashes\033[0;37m) {grey}> {white}").lower() 
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        # Misc Options
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back']: main()
        elif cho in ['help', '?', '??']: helpsub_manual()
        elif cho in ['opt', 'options']: hashing_submenu_manual()
        elif cho in ["exec", "e"]: os.system(fullcho[5:]) if cho == "exec" else os.system(fullcho[2:])
        # Commands
        elif cho in ['md5', '0']: hashes.hashing("md5")
        elif cho in ['sha1','1']: hashes.hashing("sha1")
        elif cho in ['sha224','2']: hashes.hashing("sha224")
        elif cho in ['sha256','3']: hashes.hashing("sha256")
        elif cho in ['sha384','4']: hashes.hashing("sha384")
        elif cho in ['sha512','5']: hashes.hashing("sha512")
        else:print(f"\n{bad} Command not found")

def webs_submenu():
    tW = 1 if os.path.exists("/data/data/com.termux") else 0
    while True:
        cho = input(f"\n \033[1m\033[4;37mskajptls{white} (\033[1;38;2;200;127;0mWebs\033[0;37m) \033[1;31mNT {grey}> {white}").lower() if os.name == 'nt' else input(f"\n \033[1m\033[4;37mskajptls{white} (\033[1;38;2;200;127;0mWebs\033[0;37m) {grey}> {white}").lower() 
        try: fullcho = cho; cho = cho.split()[0]
        except: pass
        if cho in ['clear', 'cls']: clear()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['back', 'b']: main()
        elif cho in ['opt', 'options']: webs_manual()
        elif cho in ['help', '?', '??', 'h']: helpsub_manual()
        elif cho in ["exec", "e"]: os.system(fullcho[5:]) if cho == "exec" else os.system(fullcho[2:])
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
        elif cho in ["pat","50"]: webbrowser.open("https://github.com/swisskyrepo/PayloadsAllTheThings"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://github.com/swisskyrepo/PayloadsAllTheThings")
        elif cho in ["checkh","51"]:webbrowser.open("https://check-host.net/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://check-host.net/")
        elif cho in ["censys","52"]: webbrowser.open("https://search.censys.io/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://search.censys.io/")
        elif cho in ["abox","53"]:webbrowser.open("https://anonbox.net/"); print('\033[1;32m' + "\n Openning browser...") if tW==0 else print('\033[1;32m' + "\n https://anonbox.net/")
        else:print(f"\n{bad} Command not found")

 ##########################################################################

def CheckForUpdates():
  f=False
  try:
    if os.name == 'nt':
      try: subprocess.check_output("ping 1.1.1.1 -n 1", shell=True);f=True
      except: f=False
      try: subprocess.check_output("ping 8.8.8.8 -n 1", shell=True);f=True
      except: f=False
    else:
      try: subprocess.check_output("ping -c 1 1.1.1.1", shell=True,stderr=subprocess.STDOUT);f=True
      except: f=False
      try: subprocess.check_output("ping -c 1 8.8.8.8", shell=True,stderr=subprocess.STDOUT);f=True
      except: f=False
    if f: 
      response = requests.get('https://pastebin.com/raw/Y4fBQP1h')
      if __version__ == int(response.text): print(f"\n{good} Up to date")
      elif __version__ > int(response.text): print(f"\n{good} Newer {grey}(testing){white}")
      else: print(f"{bad}\n Old")
    else: print(f"\n{bad} No internet connection\n{bad} Some features may not work properly"); time.sleep(2)
  except: print(f"\n{bad} No internet connection\n{bad} Some features may not work properly"); time.sleep(2)

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
    if not f:return True if input(f"\n{bad} No internet connection detected, would you want to bypass it? {grey}(Y/N):{white} ").lower() == "y" else False
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
    if logo_type == "random": logo_col1 = random.randrange(60, 255); logo_col2 = random.randrange(60, 255); logo_col3 = random.randrange(60, 255)
    if logo_type == "static": cR, cG, cB = LoadSettings("cols"); logo_col1 = int(cR); logo_col2 = int(cG); logo_col3 = int(cB)
    print(f"""\033[1;38;2;{logo_col1};{logo_col2};{logo_col3}m
       _____ __           _          ________   _____
      / ___// /______ _  (_)___     /_  __/ /  / ___/
      \__ \/ //_/ __ `/ / / __ \     / / / /   \__ \ 
     ___/ / ,< / /_/ / / / /_/ /    / / / /______/ / 
    /____/_/|_|\__,_/_/ / .___/    /_/ /_____/____/  
                   /___/_/                          
                                {grey}By Skajp
    """)
    print(f"{grey} Version: {__version__}")
    print(f"{grey} Type 'help' or '?' to show help menu{white}")
    main()

def StartLOL(opt, fullcho):
  if opt == "pscan":
    if len(fullcho.split(" ")) == 3:
      if fullcho.split(" ")[0] == "pscan":
        ips = fullcho[6:].split(" ")[0]
        ports = int(fullcho[6:].split(" ")[1])
        print(ips, ports)
        pscan.main(ips,ports)
      else:
        print(fullcho[2:])

def chat_submenu():OnlineChat.Menu();main()

def main():
    while True:
        cho = input(f"\n \033[1m\033[4;37mskajptls{white} \033[1;31mNT {grey}> {white}").lower() if os.name == 'nt' else input(f"\n \033[1m\033[4;37mskajptls{white} {grey}> {white}").lower() 
        try: fullcho = cho;cho = cho.split()[0]
        except: pass
        # options
        if cho in ['r']: clear(); logo()
        elif cho in ['exit', 'quit', 'q']: quit()
        elif cho in ['clear', 'cls']: clear()
        elif cho in ['settings','set']: Settings_menu()
        # Manuals
        elif cho in ['help', '?', '??',"h"]: help_manual()
        elif cho in ['opt', 'options']: options_manual()
        elif cho in ["exec", "e"]: os.system(fullcho[5:]) if cho == "exec" else os.system(fullcho[2:])
        # Imported modules from ./misc/modules/
        elif cho in ['pscan','p','0']: pscan.main() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['geoip','iplookup','iplook','ip','1']: iplookup.IPLookUp() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['macl','maclookup', '2']: maclookup.MacAddrLookUp() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['myip', '3']: getip.myip() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['aftp', '4']: anonftp.FTPanonLOG() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['mailscraper','mailscrape','m','5']: mailscrape.EmailScrape() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['chat', '6']: chat_submenu() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['pyobs', '7']: obs.Obs()
        elif cho in ['keylog', '8']: keylogger.Keylogger() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['chmac','9']: changemac.main()
        # Functions from this file
        # Submenus
        elif cho in ['webs', 'web','10']: webs_submenu() if InChck() else print("\033[1;31m\n No internet connection")
        elif cho in ['hash','11']: hashing_submenu()
        elif cho in ['mac', '12']: ChangeMacSubmenu()
        else:print(f"\n{bad} Command not found")


def FirstStart():
  def GetPipVer():return float(subprocess.check_output("pip --version",shell=True,stderr=subprocess.STDOUT).decode().split(" ")[1])
  Reqs = []
  try:
    with open("requirements.txt") as f:
      for i in f.readlines(): Reqs.append(i[:-1])
  except: clear();print(f"{bad} Failed to locate 'requirements.txt' folder");time.sleep(5);quit()

  for i in Reqs:
    print(f"{status} Installing{grey}:{white} {i}        ", end="\r")
    subprocess.call(f"pip install {i} >nul", shell=True, stdout=FNULL, stderr=subprocess.STDOUT) if os.name == 'nt' else subprocess.call(f"pip install {i} --break-system-package", shell=True, stdout=FNULL, stderr=subprocess.STDOUT) if GetPipVer() >= 23.0 else subprocess.call(f"pip install {i}", shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    print(f"{good} Installed{grey}:{white} {i}         ")

  os.mkdir('./misc/chats')
  os.mkdir('./misc/keylogger')
  os.mkdir('./misc/keylogger/clients')
  os.mkdir('./misc/keylogger/logs')
  os.mkdir('./misc/mails') 
  open('./misc/.a','x')

  import random, threading, concurrent.futures, requests, datetime, base64, codecs, string, json, socket, urllib.parse, re, webbrowser, platform, shutil
  from bs4 import BeautifulSoup
  from collections import deque
  from async_timeout import timeout
  CheckForUpdates(); main()

if __name__ == "__main__":
  if sys.platform == "linux":
    if not os.path.exists("./misc/.a"):
      print(f"{status} Welcome to SkajpTLS, i hope that you will like it! :)\n{status} I will set everything up for you, just wait a second...\n")
      FirstStart()
    else: 
      import random, threading, concurrent.futures, requests, datetime, base64, codecs, string, json, socket, urllib.parse, re, webbrowser, platform, shutil
      from bs4 import BeautifulSoup
      from collections import deque
      from async_timeout import timeout
      CheckForUpdates(); logo()

  elif sys.platform == "darwin":
    if not os.path.exists("./misc/.a"):
      print(f"{status} Welcome to SkajpTLS, i hope that you will like it! :)\n{status} I will set everything up for you, just wait a second...\n")
      FirstStart()
    else: 
      import random, threading, concurrent.futures, requests, datetime, base64, codecs, string, json, socket, urllib.parse, re, webbrowser, platform, shutil
      from bs4 import BeautifulSoup
      from collections import deque
      from async_timeout import timeout
      CheckForUpdates(); logo()

  elif sys.platform == "win32":
    if not os.path.exists("./misc/.a"):
      print(f"{status} Welcome to SkajpTLS, i hope that you will like it! :)\n{status} I will set everything up for you, just wait a second...\n")
      FirstStart()
    else: 
      import random, threading, concurrent.futures, requests, datetime, base64, codecs, string, json, socket, urllib.parse, re, webbrowser, platform, shutil
      from bs4 import BeautifulSoup
      from collections import deque
      from async_timeout import timeout
      CheckForUpdates(); logo()

  else:print(f"{bad} Can't determine")
