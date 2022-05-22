import pyjokes
import soundManager as sm


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
       joke = pyjokes.get_joke(language='es')
       sm.Mixer().playVoice(joke)

    @staticmethod
    def skill_output():
        pass

    @staticmethod
    def kill():
        pass