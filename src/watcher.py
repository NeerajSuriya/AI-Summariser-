import time
import os 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "resumes/queue"

class ResumeHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(".pdf"):
            filename = os.path.basename(event.src_path)
            print(f"[Watcher] File detected: {filename}") 
            self.callback(filename)

def start_watcher(callback):
    event_handler = ResumeHandler(callback)
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()
    print(f"[Watcher] Watching folder: {WATCH_FOLDER}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

