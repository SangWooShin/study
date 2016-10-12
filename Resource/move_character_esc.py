from pico2d import *

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

open_canvas()
MainCharacter = load_image('MainCar.png')
AiCharacter = load_image('PoliceCar.png')

running = True
y = 0
frame = 0
while (y < 600 and running):
    clear_canvas()
    MainCharacter.clip_draw(0, 0, 100, 100, 400, y)
    AiCharacter.clip_draw(frame*100, 0, 100, 100, 300, y)
    update_canvas()
    frame = (frame + 1) % 8
    y += 5
    delay(0.1)
    handle_events()

close_canvas()

