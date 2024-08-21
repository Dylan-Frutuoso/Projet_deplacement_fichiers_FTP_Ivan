import os
import shutil
import time

# Définir les répertoires source et de destination
source_dir = "C:\\Users\\DylanFRUTUOSO\\OneDrive - DGS TRANSPORTS\\Bureau\\projets-python\\Projet_Ivan_scan_fichier_ftp\\TEST DEPLACEMENT FICHIER SOURCE AVEC PYTHON"
destination_dir = "C:\\Users\\DylanFRUTUOSO\\OneDrive - DGS TRANSPORTS\\Bureau\\projets-python\\Projet_Ivan_scan_fichier_ftp\\TEST DEPLACEMENT FICHIER DESTINATION AVEC PYTHON"

# Définir une fonction pour déplacer les fichiers du répertoire source vers le répertoire de destination
def move_files():
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        shutil.move(source_file, destination_file)

# Exécuter la fonction toutes les 5 secondes
while True:
    move_files()
    time.sleep(5)

