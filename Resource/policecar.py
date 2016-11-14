import random
from pico2d import *

class Policecar:

    image = None
    def __init__(self):
        global direction, movex, init, score, scoretime
        direction = 0
        movex = 0
        init = 0
        score = 0
        scoretime = 0
        self.rand = random.randint(1, 6)
        if self.rand == 1:
            self.x = 100
        elif self.rand == 2:
            self.x = 150
        elif self.rand == 3:
            self.x = 250
        elif self.rand == 4:
            self.x = 350
        elif self.rand == 5:
            self.x = 440
        elif self.rand == 6:
            self.x = 480

        self.y = 1000
        self.frame = 0
        if Policecar.image == None:
            Policecar.image = load_image('PoliceCar.png')

    def update(self):
        global  direction, movex, init, score, scoretime
        if direction == 0:
            movex += 0.1
            if movex > 60:
                direction = 1
        else:
            movex -= 0.1
            if movex < -60:
                direction = 0
        self.frame = (self.frame + 1) % 2
        if self.y < 65:
            self.y = 1200
        if score % 100 == 0:
            init = 1

        if init == 1:
            self.y -= 0.05

        scoretime += 1
        score = int(scoretime / 400)

    def draw(self):
        global movex
        self.image.clip_draw(self.frame * 150, 0, 150, 150, self.x + movex, self.y)

    def get_bb(self):
        return self.x - 30 + movex, self.y - 65, self.x + 30 + movex, self.y + 60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())