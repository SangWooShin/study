from pico2d import *

class Road:

    image = None;

    def __init__(self):
        self.x, self.y = 300, 200
        if Road.image == None:
            Road.image = load_image('Road.png')

    def update(self):
        self.y -= 1
        if self.y == -200:
            self.y = 800

    def draw(self):
        self.image.draw(self.x, self.y)