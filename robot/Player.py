import subprocess
import threading
import os
from robot import utils

def play(src, delete=False):
    foo, ext = os.path.splitext(src)
    if ext in ('.wav', '.mp3'):
        player = SoxPlayer()
        player.play(src, delete)

class AbstractPlayer(threading.Thread):

    def play(self, src):
        pass


class SoxPlayer(AbstractPlayer):

    def __init__(self):
        super(SoxPlayer, self).__init__()
        self.playing = False

    def run(self):
        cmd = ['play', self.src]
        self.proc = subprocess.Popen(cmd)
        self.playing = True
        self.proc.wait()
        self.playing = False
        if self.delete:
            utils.check_and_delete(self.src)

    def play(self, src, delete=False):
        self.src = src
        self.delete = delete
        self.start()

    def stop(self):
        if self.proc and self.playing:
            self.proc.terminate()
            if self.delete:
                utils.check_and_delete(self.src)