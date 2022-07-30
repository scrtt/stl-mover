import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from mover import Mover

INCOMING_PATH = os.path.join(os.environ['USERPROFILE'], 'Downloads')
STL_PATH = 'P:\\stl'


class Watcher:

    def __init__(self):
        self.observer = Observer()

    def run(self):
        handler = FileHandler()
        self.observer.schedule(handler, INCOMING_PATH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("There is an Error")

        self.observer.join()


class FileHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        time.sleep(2)  # Waiting for chrome virus scan
        Mover(INCOMING_PATH, STL_PATH, 'stl').move()


if __name__ == '__main__':
    w = Watcher()
    w.run()
