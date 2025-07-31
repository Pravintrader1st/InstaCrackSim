# instagram_cracker_sim.py

import time
import os

# Fake user database for simulation
fake_users = {
    "now_for_cyber199": "a490zl0i",
    "admin": "admin2024"
}

# Logo
logo = r'''
  ___           _                       _
 |_ _|_ __  ___| |_ ___  _ __ ___   ___| |_ ___  _ __
  | || '_ \/ __| __/ _ \| '_ ` _ \ / _ \ __/ _ \| '__|
  | || | | \__ \ || (_) | | | | | |  __/ || (_) | |
 |___|_| |_|___/\__\___/|_| |_| |_|\___|\__\___/|_|

             Instagram Password Cracker [SIMULATION]
''' 
# Function to check login (simulated)
def check_login(username, password):
    return fake_users.get(username) == password

# Show logo
os.system("clear")  # Use 'cls' if on Windows
print(logo)
print("-" * 60)

# Get user input
username = input("Enter Instagram username: ").strip()
wordlist_path = input("Enter path to wordlist file (or press Enter for default): ").strip()

# Use default if nothing entered
if not wordlist_path:
    wordlist_path = "wordlist_numbered.txt"

# Load passwords
try:
    with open(wordlist_path, "r") as f:
        passwords = f.read().splitlines()
except FileNotFoundError:
    print(f"[!] Wordlist file not found: {wordlist_path}")
    exit()

# Simulated cracking process
print("\n[~] Starting password attack...")
time.sleep(1)

for pwd in passwords:
    print(f"[*] Trying password: {pwd}")
    time.sleep(0.01)

    if check_login(username, pwd):
        print(f"\n[+] Password found for @{username}: {pwd}")
        break
else:
    print(f"\n[-] Password not found in wordlist for @{username}")
