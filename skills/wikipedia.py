import wikipedia
import intent
import soundManager as sm

wikipedia.set_lang("es")


#class Skill(threading.Thread):
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
        search = intent.placeHolders['search']
        try:
            result = wikipedia.summary(search, sentences=1)
            print(result)
            sm.Mixer().playVoice(result)
        except wikipedia.exceptions.DisambiguationError as error:
            print("Muchos resultados coincidentes, se mas preciso anda")
            pass
        except Exception as e:
            print("He petao")
            pass

    @staticmethod
    def skill_output():
        pass
    
    @staticmethod
    def kill():
        pass
