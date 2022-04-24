import Speak as sp
from threading import Thread
import pyaudio
import struct
import pvporcupine
import speech_recognition as sr

import dbcontroller as db


class Main(Thread):
    # Variables del objeto porcupine que nos permite obtener y procesar el wakeword
    path_custom_word = 'picovoice/wake_word/Hey-Kaplan_es_windows_v2_1_0.ppn'

    porcupine = pvporcupine.create(
        access_key='OZWTKpdX4XPqZaPS5JM76gPLBCkc5Bk6sqWgq+mMmonoZ2Mlj7HcfQ==',
        keyword_paths=['picovoice/wake_word/Hey-Kaplan_es_windows_v2_1_0.ppn'],
        model_path='picovoice/wake_word/porcupine_params_es.pv'
    )

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=porcupine.sample_rate,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

    def __init__(self):
        Thread.__init__(self)
        self.running = True
        self.run()

    def get_next_audio_frame(self):
        # Método que devuelve el stream por audio_frame del microfono
        # Captura del audio del microfono
        return self.stream

    def run(self):
        
        recognizer = sr.Recognizer()

        while self.running:
            stream = self.get_next_audio_frame()
            pcm = stream.read(self.porcupine.frame_length)
            pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
            keyword_index = self.porcupine.process(pcm)
            if keyword_index >= 0:
                print("Hola, que deseas?")

                with sr.Microphone() as source:
                    try:
                        audio = recognizer.listen(source)
                        text = recognizer.recognize_google(audio, language="es-ES")
                        print(text)
                    except:
                        print("Lo siento, no te he entendido")

        self.porcupine.delete()

    def stop(self):
        self.running = False

main = Main()

#a = Main()
b = sp.Speaker()

#a.start()
b.start()
