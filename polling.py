import os
from client import Client

class pollin(object):
    def __init__(self):
        self._cached_stamp = 0
        self.filename = 'client_data/index.html'
        self.file = Client()

    def run(self):
        while True:
            stamp = os.stat(self.filename).st_mtime
            if stamp != self._cached_stamp:
                self._cached_stamp = stamp
                # File has changed, so do something...
                print("file has been modified")
                self.file.run()


check = pollin()
check.run()