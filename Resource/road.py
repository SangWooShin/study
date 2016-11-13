from pico2d import *

class Ball:

    image = None;

    def __init__(self):
        self.x, self.y = 400, 200
        if Ball.image == None:
            Ball.image = load_image('Road.png')

    def update(self, frame_time):
        self.y -= 1

    def draw(self):
        self.image.draw(self.x, self.y)