#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp

def EmailScrape():
    import re, requests, urllib.parse, datetime
    from collections import deque
    from bs4 import BeautifulSoup
    user_url = str(input('\033[1;93m' + "\n URL" + '\033[1;90m' + " > " + '\033[0m' +f""))
    while "http" not in user_url:user_url = str(input('\033[1;93m' + " URL (with \033[1;33mhttps://\033[0m or \033[1;33mhttps://\033[0m)" + '\033[1;90m' + " > " + '\033[0m' +f""))
    count_stop = int(input('\033[1;93m' + " Links To Scan" + '\033[1;90m' + " > " + '\033[0m' +f""))
    print('\033[1;33m' + "\n Scanning" + '\033[1;90m' + " > " + '\033[0m' +f"{user_url}\n")
    urls = deque([user_url])
    scraped_urls = set()
    emails = set()
    count = 0
    try:
        while len(urls):
            count += 1
            if count == count_stop:break
            url = urls.popleft()
            scraped_urls.add(url)
            parts = urllib.parse.urlsplit(url)
            base_url = '{0.scheme}://{0.netloc}'.format(parts)
            path = url[:url.rfind('/')+1] if '/' in parts.path else url
            print('\033[1;90m' + f" \033[0;93m{count}\033[0;90m > " + '\033[0;37m' +f"{url}")
            try:response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):continue
            new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
            emails.update(new_emails)
            soup = BeautifulSoup(response.text, features="lxml")
            for anchor in soup.find_all("a"):
                link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
                if link.startswith('/'):link = base_url + link
                elif not link.startswith('http'):link = path + link
                if not link in urls and not link in scraped_urls:urls.append(link)
    except KeyboardInterrupt:print('\033[1;31m' + ' Stopping');quit()
    except ValueError():pass
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    timen = datetime.datetime.now().strftime('%Hh %Mm %Ss')
    filename = f'misc/mails/{date} ({timen}).txt'
    try:
        fp = open(filename, 'x')
        fp.close()
    except:
        try:
            fp = open(f"1_{filename}", 'x')
            fp.close()
        except:
            try:
                fp = open(f"2_{filename}", 'x')
                fp.close()
            except:
                fp = open(f"3_{filename}", 'x')
                fp.close()
    foundm = []; idk = []
    for i in emails:
        a = i.split(".")
        a.reverse()
        if not a[0] in ["jpg", "png", "gif", "webm", "mp4", "mp3", "av1", "svg", "webp", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "html", "css", "js", "json", "xml", "csv", "sql", "php", "java", "cpp", "c", "py", "rb", "go", "swift", "ts", "md", "yaml", "ini", "cfg", "bat", "sh", "ps1", "dll", "exe", "tar", "zip", "rar", "7z", "gz", "bz2", "xz", "iso", "bin", "dmg", "apk", "deb", "rpm", "img", "iso"]:idk.append(i)
    print('\033[1;93m' + "\n\n Mails Found" + '\033[1;90m' + " > " + '\033[0;37m' +f"{len(idk)}\n")
    for mail in idk:
        foundm.append(f"\n{mail}")
        print('\033[1;90m' + " > " + '\033[0;37m' +f"{mail}")
    with open(filename, 'w') as f:
        bruh = '#' * len(user_url)
        f.write(f'################ {user_url} ################')
        f.writelines(foundm)
        f.write(f'\n#################{bruh}#################')
    f.close
