from pico2d import *
class Maincar:

    PIXEL_PER_METER = (10.0 / 0.3)          # 10 pixel 30cm
    RUN_SPEED_KMPH = 50.0                   # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    image = None

    def __init__(self):
        self.x, self.y = 450, 80
        self.life = 10
        self.leftmove = 0
        self.rightmove = 0
        self.upmove = 0
        self.downmove = 0
        self.dir = 0
        self.ydir = 0
        if Maincar.image == None:
            Maincar.image = load_image('MainCar.png')
        self.crushsound = load_wav('CarHit.wav')
        self.crushsound.set_volume(40)
        self.eatitemsound = load_wav('EatItem.wav')
        self.eatitemsound.set_volume(40)

    def crush_sound(self):
        self.crushsound.play()

    def eatitem_sound(self):
        self.eatitemsound.play()



    def update(self, frame_time):
        if  self.x < 50 and self.dir == -1:  # 차량움직임
            self.dir = 0
        elif  self.x > 550 and self.dir == 1:  # 차량움직임
            self.dir = 0
        distance = Maincar.RUN_SPEED_PPS * frame_time
        self.x += (self.dir * distance)

    def draw(self):
        self.image.clip_draw(0, 0, 150, 150, self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 65, self.x + 30, self.y + 60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())