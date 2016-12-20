from pico2d import *

class Road:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 40.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None;

    def __init__(self):
        self.x = 300
        self.y = 0
        if Road.image == None:
            Road.image = load_image('Road.png')

    def update(self, frame_time, boostspeed):
        if(self.y < -200) :
            self.y += 800
        distance = Road.RUN_SPEED_PPS * frame_time
        self.y -= boostspeed * distance



    def draw(self):
        self.image.draw(self.x, self.y)