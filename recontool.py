import subprocess
import os
from colorama import Fore, Style, init

# Initialiser Colorama
init(autoreset=True)

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8')

def save_output(filename, content):
    with open(filename, "w") as f:
        f.write(content)

# Affichage du logo avec couleurs
print(Fore.GREEN + r"""
 ____                        _____           _ 
|  _ \ ___  ___ ___  _ __   |_   _|__   ___ | |
| |_) / _ \/ __/ _ \| '_ \    | |/ _ \ / _ \| |
|  _ <  __/ (_| (_) | | | |   | | (_) | (_) | |
|_| \_\___|\___\___/|_| |_|   |_|\___/ \___/|_|
""" + Style.RESET_ALL)

print(Fore.YELLOW + "[*] Initialisation...")
print(Fore.YELLOW + "[*] Chargement des modules...")
print(Fore.CYAN + "[*] Démarrage de la reconnaissance...")
print(Fore.GREEN + "[*] Bonne chasse !")

# Dessin amusant
print(Fore.MAGENTA + r"""
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
""")

# Demander la cible
target = input("Entrez l'adresse IP ou le domaine de la cible : ")

# Définir le répertoire de sortie
output_dir = "recon_results"

# Créer le répertoire s'il n'existe pas
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Démarrage de la reconnaissance...")

# Nmap
print("Exécution de Nmap...")
nmap_output = run_command(f"nmap -A -p- -sV -sC {target}")
save_output(f"{output_dir}/nmap_results.txt", nmap_output)

# Wafw00f
print("Exécution de Wafw00f...")
waf_url = "http://{target}"
wafw00f_output = run_command(f"wafw00f {waf_url}")
save_output(f"{output_dir}/wafw00f_results.txt", wafw00f_output)

# CORScanner
print("Exécution de CORScanner...")

corscanner_path = "./cors-scanner/cors_scan.py"  # Chemin relatif vers le script

if os.path.exists(corscanner_path):
    corscanner_output = run_command(f"python3 {corscanner_path} -u http://{target}")
    save_output(f"{output_dir}/corscanner_results.txt", corscanner_output)
else:
    print(f"{Fore.RED}[!] Le fichier {corscanner_path} est introuvable. Assurez-vous que CORScanner est cloné dans ./cors-scanner/")


# Gobuster
print("Exécution de Gobuster...")
gobuster_output = run_command(f"gobuster dir -u http://{target} -w /usr/share/wordlists/dirb/common.txt")
save_output(f"{output_dir}/gobuster_results.txt", gobuster_output)

# Nikto
print("Exécution de Nikto...")
nikto_output = run_command(f"nikto -h http://{target}")
save_output(f"{output_dir}/nikto_results.txt", nikto_output)

print(f"Reconnaissance terminée. Les résultats sont sauvegardés dans le dossier {output_dir}")
