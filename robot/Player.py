import subprocess
import threading
import os

def play(src, delete=False):
    foo, ext = os.path.splitext(src)
    if ext in ('.wav', '.mp3'):
        player = SoxPlayer()
        player.play(src, delete)

class AbstractPlayer(threading.Thread):

    def play(self, src):
        pass


class SoxPlayer(AbstractPlayer):

    def run(self):
        cmd = ['play', self.src]
        subprocess.run(cmd)
        if self.delete:
            if os.path.exists(self.src):
                os.remove(self.src)

    def play(self, src, delete=False):
        self.src = src
        self.delete = delete
        self.start()