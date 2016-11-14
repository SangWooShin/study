from pico2d import *

class Maincar:

    image = None

    def __init__(self):
        self.x, self.y = 450, 80
        self.life = 5
        if Maincar.image == None:
            Maincar.image = load_image('MainCar.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 150, 150, self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 65, self.x + 30, self.y + 60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())