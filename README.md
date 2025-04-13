# 🛠️ Recon Automation Tool

Un outil Python d'automatisation pour la reconnaissance réseau, incluant des outils populaires comme Nmap, Wafw00f, Gobuster, Nikto, et CORScanner.

## 🚀 Fonctionnalités

- **Nmap** : Scan de services et versions sur la cible.
- **Wafw00f** : Détection du pare-feu d'application web.
- **CORScanner** : Vérification des vulnérabilités CORS.
- **Gobuster** : Bruteforce des répertoires sur la cible.
- **Nikto** : Scan des vulnérabilités web courantes.

## Installer les outils externes 


## 🛠️ Installation recontool.py

Nmap: 
  sudo apt-get install nmap
Wafw00f:
  pip install wafw00f
CORScanner: Clonez le projet GitHub :
  git clone https://github.com/EdOverflow/cors-scanner
  cd cors-scanner
  python3 setup.py install
Gobuster: 
  sudo apt-get install gobuster
Nikto: 
  git clone https://github.com/sullo/nikto.git
  cd nikto
  perl nikto.pl


1. Clonez le dépôt :  
```bash
git clone https://github.com/kentch4n/recon-tool.git
cd recon-tool
python3 recontool.py 
