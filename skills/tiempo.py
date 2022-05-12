import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

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
        # Search for current weather in London (Great Britain) and get details
        observation = mgr.weather_at_place(intent.placeHolders['city'])
        w = observation.weather

        # w.detailed_status  # 'clouds'
        # w.wind()  # {'speed': 4.6, 'deg': 330}
        # w.humidity  # 87
        # w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        # w.rain  # {}
        # w.heat_index  # None
        # w.clouds  # 75

        return w

    @staticmethod
    def skill_output():
        pass

    @staticmethod
    def kill():
        pass
