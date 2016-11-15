import game_framework
from pico2d import *
import main_state
import json
import title_state
import game_framework

name = "RankingState"
image = None
font = None

def enter():
    global image, font
    image = load_image('blackboard.png')


def exit():
    global image
    del(image)


def pause():
    pass

def resume():
    pass

def bubble_sort(data):
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            if data[i]['Score'] < data[j]['Score']:
                data[i], data[j] = data[j], data[i]

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)



def update(frame_time):
    pass

def draw_ranking():
    f = open('data_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)
    score_data = score_data[:10]

    font = load_font('ENCR10B.TTF', 80)
    font.draw(140, 550, '[GAME OVER]', (255, 255, 255))
    font = load_font('ENCR10B.TTF', 40)
    font.draw(200, 470, 'YOUR SCORE :', (255, 0, 0))
    font.draw(500, 470, '%3d' % main_state.score, (255, 0, 0))

    font = load_font('ENCR10B.TTF', 30)
    font.draw(300, 420, 'RANKING', (255, 255, 255))
    y = 0
    font = load_font('ENCR10B.TTF', 20)
    for score in score_data:
        font.draw(150, 370 - 30 * y, 'Score :  %3d' % score['Score'], (255, 255, 255))
        y += 1

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    draw_ranking()
    update_canvas()