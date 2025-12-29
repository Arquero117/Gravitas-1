import pyxel
import settings
from classes.game import Game

class App:
    def __init__(self):

        pyxel.init(settings.WIDTH, settings.HEIGHT, title=settings.TITLE, fps=settings.FPS)
        
        self.current_scene = Game()
        
        pyxel.run(self.update, self.draw)

    def update(self):
        self.current_scene.update(self)

    def draw(self):
        self.current_scene.draw()