from doctest import FAIL_FAST
from io import BytesIO
from AudioFile import AudioFile
from vlcPlayer import vlcPlayer
import time
from gtts import gTTS
from pydub import AudioSegment
import pygame.mixer as pymixer


class Mixer(object):
    __instance = None

    def __new__(cls):
        print("New")
        if Mixer.__instance is None:
            Mixer.__instance = object.__new__(cls)
        return Mixer.__instance

    def __init__(self) -> None:
        # 0 = Voice, 1 = System, 2 = Other
        pymixer.init()

    def playUrl(self, url):
        try:
            del self.d
        except Exception as e:
            pass
        self.d = vlcPlayer(url)
        self.d.start()

    def playVoice(self, text):
        pymixer.music.stop()
        mp3_fp = BytesIO()
        tts = gTTS(text, lang="es-es", slow=False)
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        sound = AudioSegment.from_file(mp3_fp)
        wav_fp = sound.export(mp3_fp, format = "wav")
        pymixer.music.load(wav_fp)
        pymixer.music.play()

    def playSys(self, file):
        pymixer.Channel(1).stop()
        pymixer.Channel(1).play(pymixer.Sound(file))

    def playOther(self, file):
        pymixer.Channel(2).stop()
        pymixer.Channel(2).play(pymixer.Sound(file))

    def stopAll(self):
        pymixer.stop()
        try:
            del self.d
        except:
            print("No he podidio parar a D")
        
        
