from pico2d import *
import game_framework
class Maincar:
    TARGET_FPS = 60.0
    TARGET_FRAME_TIME = 1.0 / TARGET_FPS

    PIXEL_PER_METER = (10.0 / 0.3)          # 10 pixel 30cm
    RUN_SPEED_KMPH = 100.0                   # Km / Hour
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
        if Maincar.image == None:
            Maincar.image = load_image('MainCar.png')


    def update(self, frame_time):


        if self.leftmove == 1 and self.x > 50:  # 차량움직임
            self.dir = -1
        elif self.rightmove == 1 and self.x < 550:
            self.x += 1.5
        elif self.upmove == 1 and self.y < 500:
            self.y += 1.5
        elif self.downmove == 1 and self.y > 80:
            self.y -= 1.5
        distance = Maincar.RUN_SPEED_PPS * game_framework.frame_time
        self.total_frames += 1.0
        self.frame = (self.frame + 1) % 8
        self.x += (self.dir * distance)

    def draw(self):
        self.image.clip_draw(0, 0, 150, 150, self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 65, self.x + 30, self.y + 60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())