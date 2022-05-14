from asyncio import constants
import threading
import time
from pydub import AudioSegment, playback
from pydub.playback import play

class AudioFile(threading.Thread):

    def __init__(self, file):
        threading.Thread.__init__(self)
        self.audio = AudioSegment.from_file(file, format="mp3")

    def run(self):
        self.play_obj = playback._play_with_simpleaudio(self.audio)
        #play(self.audio)

    def kill(self):
        self.play_obj.stop()
    
    def __del__(self):
        self.kill()