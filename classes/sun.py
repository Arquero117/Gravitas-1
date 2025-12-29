from classes.astra import Astra

class Sun(Astra):
    def __init__(self, name, mass, radius, x, y, sprites):
        super().__init__(name, mass, radius, x, y, sprites)
        