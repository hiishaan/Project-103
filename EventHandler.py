import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
source = "C:/Ishaan/"

class EventHandler(FileSystemEventHandler):
    
    def on_created(self,event):
        print(event)
    def on_modified(self,event):
        print(event)
    def on_moved(self,event):
        print(event)
    def on_deleted(self,event):
        print(event)

event = EventHandler()

observer = Observer()

observer.schedule(event, source, recursive=True)

observer.start()

while True:
    time.sleep(2)
    print("running...")

