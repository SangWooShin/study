from pico2d import *

running = None

class Road:
    image = None

    def __init__(self):
        self.x, self.y = 400, 400
        self.run_frames = 0
        if Road.image == None:
            Road.image == load_image('Road.png')


    def draw(self):
        pass
        self.image.clip_draw(0, 0, 150, 150, self.x, self.y)

class MainCar:
    image = None

    def __init__(self):
        self.x, self.y = 450, 80
        self.run_frames = 0
        if MainCar.image == None:
            MainCar.image = load_image('MainCar.png')


    def draw(self):
        self.image.clip_draw(0, 0, 150, 150, self.x + iX, self.y)

class AiCar:
    pass

def handle_events():
    global running
    global iX
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
    pass

def main():

    open_canvas()

    road = Road()
    maincar = MainCar()

    global running
    running = True
    global iX
    global iY
    iX = 0
    iY = 0
    while running:
        handle_events()
        road.draw()
        maincar.draw()
        update_canvas()
        iY -= 5
        delay(0.01)

    close_canvas()

if __name__ == '__main__':
    main()
