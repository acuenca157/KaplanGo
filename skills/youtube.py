import os

import youtube_dl
import re
from urllib import parse, request
import soundManager as sm
import time

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
        # obtenemos la busqueda por voz
        search = intent.placeHolders['song']

        # preparamos el parametro de la url
        query_string = parse.urlencode({'search_query': search})

        # obtenemos los resultados del html de la busqueda
        html_content = request.urlopen('https://www.youtube.com/results?' + query_string)

        # obtenemos el id de todos los videos de la busqueda
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())

        # reconstruimos la url del primer video
        video_url = "https://www.youtube.com/watch?v="+"{}".format(search_results[0])

        # pasamos la url a VLC y se reproduce.
        with youtube_dl.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', None)
            sm.Mixer().playVoice(f"Reproduciendo {video_title}")
            
        time.sleep(6.5)
        sm.Mixer().playUrl(video_url)

    @staticmethod
    def skill_output():
        pass

    @staticmethod
    def kill():
        pass
