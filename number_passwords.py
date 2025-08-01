  GNU nano 8.5                             number_passwords.py
# number_passwords.py

with open("wordlist_numbered.txt", "r") as infile:
    lines = infile.read().splitlines()

with open("wordlist_numbered.txt", "w") as outfile:
    for i, line in enumerate(lines, 1):
        outfile.write(f"{i}. {line}\n")

print("[+] Saved numbered wordlist to wordlist_numbered.txt")
