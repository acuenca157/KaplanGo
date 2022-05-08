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
        result = wikipedia.summary(search)
        print(result)
        try:
            sm.Mixer().playVoice(result)
        except:
            print("He petao")
            pass

    @staticmethod
    def skill_output():
        pass
    
    @staticmethod
    def kill():
        pass
