#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp

def KaliNgrok(): import os; os.system(""""curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok""")
def KaliAtom(): import os; os.system("""sudo apt update && sudo apt install wget gpg -y && sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list' && curl -fsSL https://packagecloud.io/AtomEditor/atom/gpgkey | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/atom-keyring.gpg && sudo apt update && sudo apt install atom -y""")