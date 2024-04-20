#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#              This script was made for Skajp TLS
#              -~==============================~-
# Made by Skajp 

def hashing(alg):
    import hashlib
    algs = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
    inp = input('\033[1;93m' + "\n String" + '\033[1;90m' + " > " + '\033[0m' +f"")
    if alg in algs: pre = hashlib.new(alg, inp.encode('utf-8')); hashed = pre.hexdigest(); print('\033[1;93m' + f"\n {alg.upper()} Hash" + '\033[1;90m' + " > " + '\033[0m' +f"{hashed}")

