import pyaudio
import wave
import threading

class AudioFile(threading.Thread):
    chunk = 1024

    def __init__(self, file, isFile = True):
        threading.Thread.__init__(self)
        """ Init audio stream """ 
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
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != b'' and self.isActive:
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

    def kill(self):
        self.isActive = False