import Speak as sp
from threading import Thread
import time
import pvporcupine
from pvrecorder import PvRecorder
import pyaudio
from pyaudio import Stream
import struct
import picovoice
from picovoice import Picovoice

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5


def wake_word_callback():
    # wake word detected
    print("Si, que deseas amo?")
    # pass


def inference_callback(inference):
    if inference.is_understood:
        intent = inference.intent
        slots = inference.slots
        print("comando detectado")
        # take action based on intent and slot values
    else:
        # unsupported command
        print("no hay comando")
        pass

class Main(Thread):

    #Variables del objeto porcupine que nos permite obtener y procesar el wakeword
    path_custom_word = 'picovoice/wake_word/Hey-Kaplan_es_windows_v2_1_0.ppn'

    handle = Picovoice(
        access_key="OZWTKpdX4XPqZaPS5JM76gPLBCkc5Bk6sqWgq+mMmonoZ2Mlj7HcfQ==",
        keyword_path=path_custom_word,
        wake_word_callback=wake_word_callback,
        context_path="picovoice/intents_sdk/KaplanTest_es_windows_v2_1_0.rhn",
        inference_callback=inference_callback,
        porcupine_model_path="picovoice/wake_word/porcupine_params_es.pv",
        rhino_model_path="picovoice/intents_sdk/rhino_params_es.pv",
        require_endpoint=True)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=handle.sample_rate,
                    input=True,
                    frames_per_buffer=handle.frame_length)

    def __init__(self):
        Thread.__init__(self)
        self.running = True

    def get_next_audio_frame(self): #Método que devuelve el stream por audio_frame del microfono
        #Captura del audio del microfono
        return self.stream

    def run(self):
        # p = pyaudio.PyAudio()
        # stream = p.open(format=pyaudio.paInt16,
        #                 channels=1,
        #                 rate=self.porcupine.sample_rate,
        #                 input=True,
        #                 frames_per_buffer=self.porcupine.frame_length)
        while self.running:
            #stream = self.get_next_audio_frame()
            # pcm = stream.read(self.porcupine.frame_length)
            # pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
            # keyword_index = self.porcupine.process(pcm)
            # if keyword_index >= 0:
            #     # detected `Hey Kaplan`
            #     # newText = input("¿Que quieres añadir?")
            #     # b.addText(newText)
            #     print("Hola, soy kaplan")
            audio_frame = self.get_next_audio_frame()
            pcm = audio_frame.read(self.handle.frame_length)
            pcm = struct.unpack_from("h" * self.handle.frame_length, pcm)
            self.handle.process(pcm)

        self.handle.delete()

    def stop(self):
        self.running = False

    """Intentamos hacer lo mismo, el wakeword y el procesamiento de intents a partir de este comentario"""


    # while True:
    #     audio_frame = get_next_audio_frame()
    #     keyword_index = porcupine.process(audio_frame)
    #     if keyword_index == 0:
    #         # detected `Hey Kaplan`
    #         # newText = input("¿Que quieres añadir?")
    #         # b.addText(newText)
    #         print("Hola, soy kaplan")


a = Main()
b = sp.Speaker()

a.start()
b.start()


