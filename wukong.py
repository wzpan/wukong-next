from snowboy import snowboydecoder
from subprocess import call
from robot import Player, ASR
import sys
import signal
import os


interrupted = False
player = None

def audioRecorderCallback(fname):
    global player
    Player.play('static/beep_lo.wav', False)
    print(ASR.transcribe(fname))

def detectedCallback():
    global player
    if player:
        player.stop()
    Player.play('static/beep_hi.wav', False)

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.38)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=detectedCallback,
               audio_recorder_callback=audioRecorderCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)

detector.terminate()