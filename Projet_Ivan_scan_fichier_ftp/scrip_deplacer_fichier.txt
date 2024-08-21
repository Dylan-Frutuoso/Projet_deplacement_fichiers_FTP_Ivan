import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MoveFileHandler(FileSystemEventHandler):
    def __init__(self, src_folder, dest_folder):
        self.src_folder = src_folder
        self.dest_folder = dest_folder

    def on_created(self, event):
        # Vérifie si l'événement concerne un fichier
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            dest_path = os.path.join(self.dest_folder, file_name)
            print(f"Déplacement du fichier {event.src_path} vers {dest_path}")
            shutil.move(event.src_path, dest_path)

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

if __name__ == "__main__":
    src_folder = "C:\\Users\\Frutuoso Dylan\\Documents\\Project_Python\\dossier_source"
    dest_folder = "C:\\Users\\Frutuoso Dylan\\Documents\\Project_Python\\dossier_destination"

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    monitor_folder(src_folder, dest_folder)