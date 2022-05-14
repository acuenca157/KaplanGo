from doctest import FAIL_FAST
from io import BytesIO
from AudioFile import AudioFile
from vlcPlayer import vlcPlayer
import time
from gtts import gTTS
from pydub import AudioSegment

class Mixer(object):

    # crear los canales
    # metodos de asignacion a los canales preestablecidos (musica, voz, sistema)
    # boton del pánico
    # atenuacion de canales
    __instance = None

    def __new__(cls):
        if Mixer.__instance is None:
            Mixer.__instance = object.__new__(cls)
        return Mixer.__instance
    
    def __init__(self) -> None:
        self.a = None # Music
        self.b = None # Voice
        self.c = None # System
        self.d = None # VLC

    def playUrl(self, url):
        try:
            del self.d
        except Exception as e:
            pass
        self.d = vlcPlayer(url)
        self.d.start()

    def playMusic(self, file):
        try:
            del self.a
        except Exception as e:
            pass
        self.a = AudioFile(file)
        self.a.start()
    
    def playVoice(self, text):
        try:
            del self.b
        except Exception as e:
            pass
        mp3_fp = BytesIO()
        tts = gTTS(text, lang="es-es")
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        self.b = AudioFile(mp3_fp)
        self.b.start()
    
    def playSys(self, file):
        try:
            del self.c
        except Exception as e:
            pass
        self.c = AudioFile(file)
        self.c.start()

    def stopAll(self):
        try:
            del self.a
        except:
            print("No he podidio parar a A")
        
        try:
            del self.b
        except:
            print("No he podidio parar a B")

        try:
            del self.c
        except:
            print("No he podidio parar a C")

        try:
            del self.d
        except:
            print("No he podidio parar a D")
