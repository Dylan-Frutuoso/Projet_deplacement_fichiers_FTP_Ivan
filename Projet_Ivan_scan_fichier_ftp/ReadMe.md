script test.py :

déplacement_fichier_automatique :

Voici une explication détaillée et simplifiée de ce code Python :

Importation des modules
Python



import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



Ces lignes importent les modules nécessaires :

- time pour gérer les pauses dans le programme.
- os pour interagir avec le système de fichiers.
- shutil pour déplacer des fichiers.
- watchdog pour surveiller les changements dans le système de fichiers.

Définition de la classe MoveFileHandler
Python

class MoveFileHandler(FileSystemEventHandler):
    def __init__(self, src_folder, dest_folder):
        self.src_folder = src_folder
        self.dest_folder = dest_folder

    def on_created(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            dest_path = os.path.join(self.dest_folder, file_name)
            print(f"Déplacement du fichier {event.src_path} vers {dest_path}")
            shutil.move(event.src_path, dest_path)


- MoveFileHandler : Une classe qui hérite de FileSystemEventHandler pour gérer les événements de création de fichiers.
- __init__ : Initialise les dossiers source et destination.
- on_created : Méthode appelée lorsqu’un nouveau fichier est créé. Si l’événement concerne un fichier (et non un dossier), le fichier est déplacé vers le dossier de destination.


Fonction monitor_folder
Python

def monitor_folder(src_folder, dest_folder):
    event_handler = MoveFileHandler(src_folder, dest_folder)
    observer = Observer()
    observer.schedule(event_handler, path=src_folder, recursive=False)
    observer.start()
    print(f"Surveillance du dossier {src_folder}. Les fichiers seront déplacés vers {dest_folder}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


- monitor_folder : Fonction qui configure et démarre la surveillance du dossier source.
- event_handler : Instance de MoveFileHandler.
- observer : Instance de Observer qui surveille les changements dans le dossier source.
- observer.schedule : Programme l’observateur pour utiliser event_handler sur le dossier source.
- observer.start : Démarre l’observateur.
- try...except : Boucle infinie pour maintenir le programme en cours d’exécution jusqu’à ce qu’il soit interrompu par l’utilisateur (Ctrl+C).


Bloc principal
Python

if __name__ == "__main__":
    src_folder = "C:\\Users\\Frutuoso Dylan\\Documents\\Project_Python\\dossier_source"
    dest_folder = "C:\\Users\\Frutuoso Dylan\\Documents\\Project_Python\\dossier_destination"

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    monitor_folder(src_folder, dest_folder)


- if __name__ == "__main__": : Vérifie si le script est exécuté directement.
- src_folder et dest_folder : Définissent les chemins des dossiers source et destination.
- os.makedirs : Crée le dossier de destination s’il n’existe pas.
- monitor_folder : Lance la surveillance du dossier source.
Ce code surveille un dossier source et déplace automatiquement tout nouveau fichier créé vers un dossier de destination.