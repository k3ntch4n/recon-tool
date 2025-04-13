🛠️ <h1 style="font-size: 22px;"> RECON TOOL </h1>

Cet outil permet d'automatiser la reconnaissance d'une cible en utilisant plusieurs outils populaires de cybersécurité et de reconnaissance. Il peut scanner à la fois des adresses IP et des domaines pour récupérer des informations détaillées sur la cible.  


🧰 **Outils utilisés dans ce script**  
  
**WHOIS** 🧐 : Obtient les informations d'enregistrement du domaine ou de l'adresse IP, telles que le registrar, les contacts, etc.  
**DIG & NSLOOKUP** 🔍 : Effectuent des requêtes DNS pour obtenir des informations détaillées sur l'adresse cible.  
**Nmap** 🕵️‍♂️ : Effectue un scan de ports avec détection des services et versions.  
**Wafw00f** 🧱 : Détecte la présence d'un pare-feu applicatif web (WAF) pour identifier les protections de la cible.  
**Gobuster** 💣 : Effectue une recherche brute de répertoires sur le site web cible.  
**Nikto** 🔒 : Scanne le site à la recherche de vulnérabilités connues et de mauvaises configurations.  
**WhatWeb** 🌐 : Identifie les technologies utilisées sur le site web de la cible.  
**Wappalyzer** 📊 : Identifie également les technologies web utilisées par le site cible.        


🚀 **Prérequis**  
Avant de lancer ce script, vous devez avoir installé les outils précédents sur votre machine, si ce n'est pas le cas utilisez les commandes suivantes :  
  ```bash
   sudo apt update
   sudo apt install whois dig nmap wafw00f gobuster nikto whatweb
  ```


🖥️ **Installation et utilisation**  
  
Étapes pour exécuter le script
Clonez ce projet ou téléchargez le fichier recon_script.py.

Exécutez le script avec Python 3 en utilisant la commande suivante :  
 ```bash
python3 recon_script.py
Le script vous demandera ensuite d'entrer une adresse IP ou un nom de domaine.
```

💻 **Exemple d'exécution**  

   Exemple 1 : Scan d'un domaine
      
      python3 recon_script.py
      Entrez l'adresse IP ou le domaine de la cible : example.com
   
   Exemple 2 : Scan d'une adresse IP  
      
      python3 recon_script.py
      Entrez l'adresse IP ou le domaine de la cible : 8.8.8.8
   
   📊 **Résultats**  
   À la fin du scan, un rapport HTML sera généré dans le répertoire recon_results/, contenant toutes les informations récupérées sur la cible. Le rapport s'appelle rapport_recon.html.


📜 Note  
Le script utilise des outils en ligne de commande, donc assurez-vous que vous avez les bonnes permissions pour les exécuter sur votre système.
