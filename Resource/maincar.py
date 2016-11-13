from pico2d import *

class Maincar:

    image = None

    def __init__(self):
        self.x, self.y = 450, 80
        if Maincar.image == None:
            Maincar.image = load_image('MainCar.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)