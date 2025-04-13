import subprocess
import os
from colorama import Fore, Style, init
import threading
import time

init(autoreset=True)

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True)
    output, _ = process.communicate()
    return output.decode('utf-8', errors='ignore')

def append_html_section(file_path, title, content):
    with open(file_path, "a") as f:
        f.write(f"""
<details>
  <summary><strong>{title}</strong></summary>
  <pre>{content}</pre>
</details>
""")

# ASCII & intro
print(Fore.GREEN + r"""
 ____                        _____           _ 
|  _ \ ___  ___ ___  _ __   |_   _|__   ___ | |
| |_) / _ \/ __/ _ \| '_ \    | |/ _ \ / _ \| |
|  _ <  __/ (_| (_) | | | |   | | (_) | (_) | |
|_| \_\___|\___\___/|_| |_|   |_|\___/ \___/|_|
""" + Style.RESET_ALL)

print(Fore.YELLOW + "[*] Initialisation...")
print(Fore.CYAN + "[*] Démarrage de la reconnaissance...")
print(Fore.GREEN + "[*] Bonne chasse !")

# Petit dessin
print(Fore.MAGENTA + r"""
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
""")

# Cible
target = input("Entrez l'adresse IP ou le domaine de la cible : ")

output_dir = "recon_results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

report_file = os.path.join(output_dir, "rapport_recon.html")

with open(report_file, "w") as f:
    f.write(f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Rapport Reconnaissance - {target}</title>
    <style>
        body {{
            background-color: #1e1e1e;
            color: #cfcfcf;
            font-family: monospace;
            padding: 20px;
        }}
        h1 {{
            color: #00ff99;
            border-bottom: 2px solid #00ff99;
            padding-bottom: 5px;
        }}
        summary {{
            cursor: pointer;
            font-size: 1.2em;
            color: #61dafb;
            margin-top: 20px;
        }}
        pre {{
            background-color: #2d2d2d;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            white-space: pre-wrap;
        }}
        details {{
            margin-bottom: 15px;
        }}
    </style>
</head>
<body>
    <h1>Rapport de Reconnaissance</h1>
    <p><strong>Cible :</strong> {target}</p>
""")

# Phase 1 - Infos DNS / WHOIS
print("[*] WHOIS...")
whois_output = run_command(f"whois {target}")
append_html_section(report_file, "WHOIS", whois_output)

print("[*] DIG...")
dig_output = run_command(f"dig {target}")
append_html_section(report_file, "DIG", dig_output)

print("[*] NSLOOKUP...")
nslookup_output = run_command(f"nslookup {target}")
append_html_section(report_file, "NSLOOKUP", nslookup_output)

# Phase 2 - Scan réseau / web
print("[*] Nmap...")
nmap_output = run_command(f"nmap -T4 -A -p- -sV -sC {target}")
append_html_section(report_file, "Nmap", nmap_output)

print("[*] Wafw00f...")
waf_output = run_command(f"wafw00f http://{target}")
append_html_section(report_file, "Wafw00f", waf_output)

print("[*] Gobuster...")
gobuster_output = run_command(f"gobuster dir -u http://{target} -w /usr/share/wordlists/dirb/common.txt")
append_html_section(report_file, "Gobuster", gobuster_output)

print("[*] Nikto...")
nikto_output = run_command(f"nikto -h http://{target}")
append_html_section(report_file, "Nikto", nikto_output)

print("[*] WhatWeb...")
whatweb_output = run_command(f"whatweb http://{target}")
append_html_section(report_file, "WhatWeb", whatweb_output)

print("[*] Wappalyzer...")
wappalyzer_output = run_command(f"wappalyzer --scan-type FULL -i http://{target}")
append_html_section(report_file, "Wappalyzer", wappalyzer_output)

# Fin HTML
with open(report_file, "a") as f:
    f.write("</body></html>")

print(Fore.GREEN + f"\n[✔] Rapport HTML généré : {report_file}")
