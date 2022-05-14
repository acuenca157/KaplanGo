import os

# import youtube_dl
from yt_dlp import YoutubeDL
import re
from urllib import parse, request
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
        search = intent.placeHolders['song']
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('https://www.youtube.com/results?' + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        video_url = "https://www.youtube.com/watch?v="+"{}".format(search_results[0])

        sm.Mixer().playUrl(video_url)

    @staticmethod
    def skill_output():
        pass

    @staticmethod
    def kill():
        pass
