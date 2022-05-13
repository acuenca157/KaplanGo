import os

import youtube_dl
import re
from urllib import parse, request

ydl_options = {
    'format': 'bestaudio/best',
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
        print(search_results)
        video_url = "https://www.youtube.com/watch?v=" + search_results[0]
        print(video_url)
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            ydl.download([video_url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")

    @staticmethod
    def skill_output():
        pass

    @staticmethod
    def kill():
        pass
