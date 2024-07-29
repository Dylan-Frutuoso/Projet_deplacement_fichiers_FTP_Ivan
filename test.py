import shutil
import os

# Chemin du fichier source"
source = "C:\\Users\\DylanFRUTUOSO\\Documents\\TEST DEPLACEMENT FICHIER AVEC PYTHON\\test_python.txt"

# Chemin du fichier de destination
destination = "C:\\Users\\DylanFRUTUOSO\\Documents\\TEST DEPLACEMENT FICHIER AVEC PYTHON 2"

# Vérifie si le fichier existe
if os.path.isfile(source):
    # Déplace le fichier
    shutil.move(source, destination)
    print("Le fichier a été déplacé avec succès.")
else:
    print("Le fichier source n'existe pas.")




