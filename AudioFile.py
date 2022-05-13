import threading
import time
from pydub import AudioSegment, playback
from pydub.playback import play

class AudioFile(threading.Thread):
    

    def __init__(self, file):
        threading.Thread.__init__(self)
        self.audio = AudioSegment.from_file(file, format="mp3")
        self.play_obj = playback._play_with_simpleaudio(self.audio)

    def run(self) -> None:
        play(self.audio)

    def kill(self):
        self.play_obj.stop()


    """

    chunk = 1024

    def __init__(self, file, isFile = True):
        threading.Thread.__init__(self)
        # Init audio stream
        self.isActive = True
        if isFile:
            self.wf = wave.open(file, 'rb')
        else:
            self.wf = file
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            #channels = self.wf.getnchannels(),
            channels = 1,
            rate = self.wf.getframerate(),
            output = True
        )
    
    def run(self):
        self.play()
        self.close()

    def play(self):
        # Play entire file
        data = self.wf.readframes(self.chunk)
        while data != b'' and self.isActive:
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        # Graceful shutdown 
        self.stream.close()
        self.p.terminate()

    def kill(self):
        self.isActive = False

    """