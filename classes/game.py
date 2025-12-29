from classes.sun import Sun
from data import SUN

class Game():
    def __init__(self):
        self.sun = Sun(*SUN.values())
    
    def update(self):
        self.sun.update()

    def draw(self):
        self.sun.draw()