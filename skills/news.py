from socket import inet_ntoa
from GoogleNews import GoogleNews
import soundManager as sm
ydl_options = {
    'format': 'mp3/bestaudio',
    'postprocessor': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }]
}


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
        word = intent.placeHolders['news']
        googlenews = GoogleNews(lang='es', period='7d', encode='utf-8')
        googlenews.search(word)
        result = googlenews.page_at(1)
        print(result)
        cont = 0
        output = "Las ultimas noticias son: "
        while cont < 3:
            output += result[cont]['title'] + ". " 
            print(result[cont]['title'])
            cont+=1
        sm.Mixer().playVoice(output)
    @staticmethod
    def skill_output():
        pass

    @staticmethod
    def kill():
        pass
