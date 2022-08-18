from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import subprocess
import platform
import glob


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename 
            os.rename(src, new_destination)
            list_of_files = glob.glob(new_destination)
            latest_file = max(list_of_files, key = os.path.getctime)
            os.startfile(latest_file)

folder_to_track = r'C:\OFX\of_v0.11.0_vs2017_release\apps\myApps\myCHURCH\bin\data'
folder_destination = r'C:\VASES'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()