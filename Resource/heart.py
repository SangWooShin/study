from pico2d import *

class Heart:

    image = None;

    def __init__(self):
        self.x, self.y = 630, 550
        self.frame = 0
        if Heart.image == None:
            Heart.image = load_image('Heart.png')


    def draw(self):
        self.image.draw(self.x, self.y)