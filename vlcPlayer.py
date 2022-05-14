import pafy
import vlc
import threading


class vlcPlayer(threading.Thread):

    def __init__(self, url):
        threading.Thread.__init__(self)
        video = pafy.new(url)
        videolink = video.getbestaudio()
        self.media = vlc.MediaPlayer(videolink.url)

    def run(self):
        self.media.play()

    def kill(self):
        self.media.stop()
    
    def __del__(self):
        self.kill()
