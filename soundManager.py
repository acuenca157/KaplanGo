from doctest import FAIL_FAST
from io import BytesIO
from AudioFile import AudioFile
from vlcPlayer import vlcPlayer
import time
from gtts import gTTS
from pydub import AudioSegment
import pygame.mixer as pymixer


class Mixer(object):
    # crear los canales
    # metodos de asignacion a los canales preestablecidos (musica, voz, sistema)
    # boton del pánico
    # atenuacion de canales
    __instance = None

    def __new__(cls):
        print("New")
        if Mixer.__instance is None:
            Mixer.__instance = object.__new__(cls)
        return Mixer.__instance

    def __init__(self) -> None:
        # 0 = Voice, 1 = System, 2 = Other
        pymixer.init()

        
        """
        self.a = None  # Music
        self.b = None  # Voice
        self.c = None  # System
        self.d = None  # VLC
        """

    def playUrl(self, url):
        try:
            del self.d
        except Exception as e:
            pass
        self.d = vlcPlayer(url)
        self.d.start()

    def playVoice(self, text):
        """try:
            del self.b
        except Exception as e:
            pass
        """
        pymixer.Channel(0).stop()
        mp3_fp = BytesIO()
        tts = gTTS(text, lang="es-es")
        tts.save("talk.mp3")
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        sound = AudioSegment.from_file(mp3_fp)
        wav_fp = sound.export(mp3_fp, format = "wav")
        pymixer.music.load(wav_fp)
        pymixer.music.play()
        # self.b = AudioFile(mp3_fp)
        # self.b.start()

    def playSys(self, file):
        pymixer.Channel(1).stop()
        pymixer.Channel(1).play(pymixer.Sound(file))
        """
        try:
            del self.c
        except Exception as e:
            pass
        self.c = AudioFile(file)
        self.c.start()
        """
    def playOther(self, file):
        pymixer.Channel(2).stop()
        pymixer.Channel(2).play(pymixer.Sound(file))

    def stopAll(self):
        pymixer.stop()
        try:
            del self.d
        except:
            print("No he podidio parar a D")

        """
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
        """
        
        
