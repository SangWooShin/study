from pico2d import *

class Box:

    image = None;

    def __init__(self):
        self.x, self.y = 200, 200
        if Box.image == None:
            Box.image = load_image('Box.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)