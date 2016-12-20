import random

from pico2d import *

class Box:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 40.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None;

    def __init__(self):
        self.randx = random.randint(1,6)
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

        self.randy = random.randint(1, 4)
        if self.randy == 1:
            self.y = 500
        elif self.randy == 2:
            self.y = 550
        elif self.randy == 3:
            self.y = 600
        elif self.randy == 4:
            self.y = 650

        if Box.image == None:
            Box.image = load_image('Box.png')

    def update(self, frame_time, boostspeed):
        if self.y < -30 or self.y == 800:
            self.randy = random.randint(1, 5)
            if self.randy == 1:
                self.y = 600
            elif self.randy == 2:
                self.y = 650
            elif self.randy == 3:
                self.y = 700
            elif self.randy == 4:
                self.y = 750
            self.randx = random.randint(1, 7)
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
        distance = Box.RUN_SPEED_PPS * frame_time
        self.y -= boostspeed * distance


    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())