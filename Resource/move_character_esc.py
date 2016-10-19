from pico2d import *

running = None

global iX
global iY

class Road:
    image = None

    def __init__(self):
        Road.image = load_image('Road.png')

    def draw(self):
        self.image.draw(400,200)

class MainCar:
    image = None

    def __init__(self):
        self.x, self.y = 450, 80
        self.frame = 0
        self.run_frames = 0
        if MainCar.image == None:
            MainCar.image = load_image('MainCar.png')



    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 150, 150, self.x + iX, self.y + iY)

class AICar:
    image = None

    def update(self):
        self.frame = (self.frame + 1) % 2

    def __init__(self):
        self.x, self.y = 170, 200
        self.frame = 0
        self.run_frames = 0
        if AICar.image == None:
            AICar.image = load_image('PoliceCar.png')

    def draw(self):
        self.image.clip_draw(self.frame * 150, 0, 150, 150, self.x + AIiX, self.y)

class Box:
    image = None

    def __init__(self):
        self.x, self.y = 450, 500
        self.frame = 0
        self.run_frames = 0
        if Box.image == None:
            Box.image = load_image('Box.png')
    def draw(self):
        self.image.clip_draw(self.frame, 0, 50, 50, self.x, self.y)

class Item:
    image = None

    def update(self):
        self.frame = (self.frame + 1) % 5

    def __init__(self):
        self.x, self.y = 640, 300
        self.frame = 0
        self.run_frames = 0
        if Item.image == None:
            Item.image = load_image('item.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    global iX
    global iY

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT and iX > -201:
                iX -= 100
            elif event.key == SDLK_RIGHT and iX < 200:
                iX += 100
            elif event.key == SDLK_UP and iY < 400:
                iY += 20
            elif event.key == SDLK_DOWN and iY > 0:
                iY -= 20
    pass

def main():

    open_canvas()

    road = Road()
    maincar = MainCar()
    aicar = AICar()
    box = Box()
    item = Item()

    global running
    running = True

    global iX
    global iY
    global AIiX
    global AIcount
    iX, iY, AIiX, AIcount = 0, 0, 0, 0

    while running:
        handle_events()
        aicar.update()
        item.update()
        road.draw()
        maincar.draw()
        aicar.draw()
        item.draw()
        box.draw()
        update_canvas()
        if AIiX > 80:
            AIcount = 1
        elif AIiX < 0:
            AIcount = 0

        if AIcount==0:
            AIiX += 10
        else:
            AIiX -= 10

        if maincar.x + iX > item.x - 75 and maincar.x + iX < item.x + 75 and maincar.y + iY > item.y - 75 and maincar.y + iY < item.y + 75:
            item.x, item.y = 650, 80

        if maincar.x + iX > aicar.x + AIiX and maincar.x + iX < aicar.x + AIiX + 75 and maincar.y + iY + 75 > aicar.y - 75 and maincar.y + iY - 50 < aicar.y + 75:
            iX, iY = 0, 0

        if maincar.x + iX > box.x - 25 and maincar.x + iX < box.x + 25 and maincar.y + iY + 75 > box.y - 25 and maincar.y + iY - 75 < box.y + 25:
            iX, iY = 0, 0

        delay(0.1)

    close_canvas()

if __name__ == '__main__':
    main()
