# 🛠️ Recon Automation Tool

Un outil Python d'automatisation pour la reconnaissance réseau, incluant des outils populaires comme Nmap, Wafw00f, Gobuster, Nikto, et CORScanner.

## 🚀 Fonctionnalités

- **Nmap** : Scan de services et versions sur la cible.
- **Wafw00f** : Détection du pare-feu d'application web.
- **CORScanner** : Vérification des vulnérabilités CORS.
- **Gobuster** : Bruteforce des répertoires sur la cible.
- **Nikto** : Scan des vulnérabilités web courantes.

## 🛠️ Installer les outils externes

Certains outils utilisés par ce script doivent être installés manuellement.

### Outils à installer :

1. **Nmap** : Utilisé pour l'analyse des services et des versions.
   - Installation sur **Ubuntu** :
     ```bash
     sudo apt-get install nmap
     ```
   
2. **Wafw00f** : Utilisé pour détecter le pare-feu d'application web.
   - Installation via `pip` :
     ```bash
     pip install wafw00f
     ```
   
3. **CORScanner** : Outil pour scanner les vulnérabilités CORS.
   - Clonez le projet GitHub :
     ```bash
     git clone https://github.com/EdOverflow/cors-scanner
     cd cors-scanner
     python3 setup.py install
     ```

4. **Gobuster** : Utilisé pour le bruteforce des répertoires.
   - Installation sur **Ubuntu** :
     ```bash
     sudo apt-get install gobuster
     ```

5. **Nikto** : Utilisé pour scanner les vulnérabilités web.
   - Installation via **GitHub** :
     ```bash
     git clone https://github.com/sullo/nikto.git
     cd nikto
     perl nikto.pl
     ```

## 🛠️ Installation du script `recontool.py`

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/kentch4n/recon-tool.git
   cd recon-tool
   python3 recontool.py 
