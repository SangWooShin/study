from pico2d import *

class MainCar:
    image = None

    #GO_LEFT, GO_STRAIGHT, GO_RIGHT = 0, 1, 2, 3

    def handle_left_go(self):
        pass
    def handle_right_go(self):
        pass

def handle_events():
    global image
    global running
    global iX
    global iXcount
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                ++iXcount
    pass

open_canvas()
MainCharacter = load_image('MainCar.png')
AiCharacter = load_image('PoliceCar.png')
running = True
iXcount = 0
y = 0
frame = 0
iX = 400 - iXcount*100
while (y < 600 and running):
    clear_canvas()
    MainCharacter.clip_draw(0, 0, 100, 100, iX, y)
    AiCharacter.clip_draw(frame*100, 0, 100, 100, 300, y)
    update_canvas()
    frame = (frame + 1) % 2
    y += 5
    delay(0.1)
    handle_events()

close_canvas()

