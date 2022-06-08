from os import O_TEMPORARY
import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import soundManager as sm

config_dict = get_default_config()
config_dict['language'] = 'es'  # your language here, eg. French

owm = OWM('446bc18cbdd7f6fa39c1cefd28cf1f69', config_dict)
mgr = owm.weather_manager()

class Skill():
    # Contruye el objeto
    def __init__(self, intent):
        self.intent = intent
        self.init(self.intent)

    # Ejecuta el hilo
    def run(self) -> None:
        self.init(self.intent)

    @staticmethod
    def init(intent):
        # Buscamos el tiempo por la ciudad que obtenemos por el comando por voz
        observation = mgr.weather_at_place(intent.placeHolders['city'])
        w = observation.weather

        # Obtenemos la descripción del tiempo
        detailed = w.detailed_status
        print(detailed)

        # Obtenemos velocidad del viento
        wind = w.wind()
        print(wind)

        # Obtenemos temperatura media en grados celsius
        temp = w.temperature('celsius')
        print(temp)

        # Formamos la cadena de salida para ser reproducida
        output = f"El tiempo actualmente es {detailed} " \
                 f"con una velocidad del viento de {wind['speed']} km/h. " \
                 f"La temperatura del ambiente es de {temp['temp']} ºC"
        print(output)
        sm.Mixer().playVoice(output)

    @staticmethod
    def skill_output():
        pass

    @staticmethod
    def kill():
        pass
