from doctest import FAIL_FAST
from io import BytesIO
from AudioFile import AudioFile
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

    def playMusic(self, file):
        if self.a is AudioFile:
            self.a.kill()
        self.a = AudioFile(file)
        self.a.start()
    
    def playVoice(self, text):
        if self.b is AudioFile:
            self.b.kill()
        mp3_fp = BytesIO()
        tts = gTTS(text, lang="es-es")
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        self.b = AudioFile(mp3_fp)
        self.b.start()
    
    def playSys(self, file):
        if self.c is AudioFile:
            self.c.kill()
        self.c = AudioFile(file)
        self.c.start()

    def stopAll(self):
        if self.a is AudioFile:
            self.a.kill()
        if self.b is AudioFile:
            self.b.kill()
        if self.c is AudioFile:
            self.c.kill()