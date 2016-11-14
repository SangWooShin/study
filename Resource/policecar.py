from pico2d import *

class Policecar:

    image = None

    def __init__(self):
        self.x, self.y = 100, 100
        self.frame = 0
        if Policecar.image == None:
            Policecar.image = load_image('PoliceCar.png')

    def update(self):
        self.frame = (self.frame + 1) % 2

    def draw(self):
        self.image.clip_draw(self.frame * 150, 0, 150, 150, self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 65, self.x + 30, self.y + 60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())