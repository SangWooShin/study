from pico2d import *

class Item:

    image = None;

    def __init__(self):
        self.x, self.y = 300, 200
        self.frame = 0
        if Item.image == None:
            Item.image = load_image('Item.png')

    def update(self):
        self.frame = (self.frame + 1) % 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)