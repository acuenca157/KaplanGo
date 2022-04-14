import Speak as sp
from threading import Thread
import time

class Main(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True

    def run(self):
        while self.running:
            newText = input("¿Que quieres añadir?")
            b.addText(newText)

    def stop(self):
        self.running = False

a = Main()
b = sp.Speaker()

a.start()
b.start()


