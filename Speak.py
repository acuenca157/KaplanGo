from queue import Queue
from threading import Thread
import time
from gtts import gTTS
import os

from mutagen.mp3 import MP3

class Speaker(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.queue = Queue()
        self.running = True

    def run(self):
        while self.running:
            if not self.queue.empty():
                text = self.queue.get()
                tts = gTTS(text, lang="es-es")
                tts.save("audio.mp3")
                os.system("start " + "audio.mp3")
                audio = MP3("audio.mp3")
                time.sleep(audio.info.length)

    def addText(self, text):
        self.queue.put(text)

    def stop(self):
        self.running = False