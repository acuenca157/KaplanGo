from asyncio import constants
import threading
import time
from pydub import AudioSegment, playback
from pydub.playback import play
import ctypes


class AudioFile(threading.Thread):

    def __init__(self, file):
        threading.Thread.__init__(self)
        self.audio = AudioSegment.from_file(file, format="mp3")

    def run(self):
        self.play_obj = playback._play_with_simpleaudio(self.audio)

    def kill(self):
        self.play_obj.stop()
        self.raise_exception()
        self.join()

    def __del__(self):
        self.kill()

    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id_thread, thread in threading._active.items():
            if thread is self:
                return id_thread

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
