from pico2d import *

class Scorescreen:

    image = None
    def __init__(self):
        self.x, self.y = 500, 300
        if Scorescreen.image == None:
            Scorescreen.image = load_image('blackboard.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
