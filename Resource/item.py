import random
from pico2d import *

class Item:

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

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
        self.y = 5000
        self.frame = 0
        if Item.image == None:
            Item.image = load_image('Item.png')

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 5
        if self.y < -40:
            self.y = 10000
        distance = Item.RUN_SPEED_PPS * frame_time
        self.y -= distance

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 40, self.x + 30, self.y + 50
