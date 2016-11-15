import random
from pico2d import *

class Heart:

    image = None;

    def __init__(self):
        self.randx = random.randint(1, 6)
        if self.randx == 1:
            self.x = 50
        elif self.randx == 2:
            self.x = 150
        elif self.randx == 3:
            self.x = 250
        elif self.randx == 4:
            self.x = 350
        elif self.randx == 5:
            self.x = 440
        elif self.randx == 6:
            self.x = 540
        self.y = 10000
        if Heart.image == None:
            Heart.image = load_image('Heart.png')

    def update(self):
        if self.y < -30 or self.y == 10000:
            self.randy = random.randint(1, 4)
            if self.randy == 1:
                self.y = 8000
            elif self.randy == 2:
                self.y = 8500
            elif self.randy == 3:
                self.y = 9000
            elif self.randy == 4:
                self.y = 9500
            self.randx = random.randint(1, 6)
            if self.randx == 1:
                self.x = 50
            elif self.randx == 2:
                self.x = 150
            elif self.randx == 3:
                self.x = 250
            elif self.randx == 4:
                self.x = 350
            elif self.randx == 5:
                self.x = 440
            elif self.randx == 6:
                self.x = 540


    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())