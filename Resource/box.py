import random

from pico2d import *

class Box:

    image = None;

    def __init__(self):
        self.rand = random.randint(1,6)
        if self.rand == 1:
            self.x = 50
        elif self.rand == 2:
            self.x = 150
        elif self.rand == 3:
            self.x = 250
        elif self.rand == 4:
            self.x = 350
        elif self.rand == 5:
            self.x = 440
        elif self.rand == 6:
            self.x = 540

        self.y = 500
        if Box.image == None:
            Box.image = load_image('Box.png')

    def update(self):
        self.y -= 1
        if self.y == 80:
            self.y = 800
            self.rand = random.randint(1, 6)
            if self.rand == 1:
                self.x = 50
            elif self.rand == 2:
                self.x = 150
            elif self.rand == 3:
                self.x = 250
            elif self.rand == 4:
                self.x = 350
            elif self.rand == 5:
                self.x = 440
            elif self.rand == 6:
                self.x = 540

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())