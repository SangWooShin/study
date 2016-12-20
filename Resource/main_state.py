import random
import json
import os

# 스크롤
# 패키징
# 속도 거리 기준 정하기
# frame 이용해서 속도 계산.
# 사운드 입히기.
from pico2d import *
from maincar import Maincar
from policecar import Policecar
from road import Road
from item import Item
from box import Box
from heart import Heart
from scorescreen import Scorescreen

import game_framework
import title_state
import ranking_state



name = "MainState"

leftmove = 0
rightmove = 0
upmove = 0
downmove = 0
score = 0
scoretime = 0



image = None
font = None


def enter():
    global maincar, policecar, road1, road2, font, boxes, item, hearts, scorescreen, boxnum, itemview, itemcount, boost, boostsave, boostspeed, heart, leftmove, rightmove, upmove, downmove, addspeed
    maincar = Maincar()
    policecar = Policecar()
    road1 = Road()
    road2 = Road()
    road2.y = 800
    boxnum = 6
    itemcount = 1
    boost = 0
    boostsave = 0
    boostspeed = 1
    addspeed = 1
    boxes = [Box() for i in range(boxnum)]
    itemview = Item()
    itemview.x = 650
    itemview.y = 350
    item = Item()
    heart = Heart()
    hearts = Heart()
    hearts.x = 650
    hearts.y = 450
    font = load_font('ENCR10B.TTF', 30)
    scorescreen = Scorescreen()
    leftmove = 0
    rightmove = 0
    upmove = 0
    downmove = 0

    game_framework.reset_time()


def pause():
    pass


def resume():
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def handle_events(frame_time):
    global leftmove, rightmove, upmove, downmove, boost, itemcount, boostsave, score
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                maincar.leftmove = 1
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                maincar.leftmove = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                maincar.rightmove = 1
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                maincar.rightmove = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                maincar.upmove = 1
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
                maincar.upmove = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                maincar.downmove = 1
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
                maincar.downmove = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
                if itemcount > 0 and boost == 0:
                    itemcount -= 1
                    boost = 1
            if maincar.life < 1:
                game_framework.change_state(ranking_state)

def update(frame_time):
    global leftmove, rightmove, upmove, downmove, score, scoretime, boxnum, boxes, itemcount, boost, boostsave, boostspeed, heart, road1, road2, addspeed
    addspeed = 1 + score / 5000
    if (boostsave) > 2000:
        boost = 0
        boostsave = 0
        boostspeed = 1
    if boost == 1:
        boostspeed = 2
        boostsave += 1
    road1.update()
    road2.update()
    for Box in boxes:
        Box.update()
    policecar.update()
    maincar.update()
    item.update()
    itemview.update()
    item.y -= 1 * boostspeed * addspeed
    road1.y -= 1 * boostspeed * addspeed
    road2.y -= 1 * boostspeed * addspeed
    heart.y -= 1 * boostspeed * addspeed
    for Box in boxes:
        Box.y -= 1 * boostspeed * addspeed
    if boost == 1:                                         # 충돌체크
        if collide(maincar, item):
            itemcount += 1
            item.y = 10000
        for Box in boxes:
            if collide(maincar, Box):
                Box.y = 800
                scoretime += 4000
        if collide(maincar, policecar):
            policecar.y = 1000
            scoretime += 40000
        if collide(maincar, heart):
            maincar.life += 1
            heart.y = 8000
    else:
        if collide(maincar, item):
            itemcount += 1
            item.y = 10000
        for Box in boxes:
            if collide(maincar, Box):
                maincar.life -= 1
                Box.y = 800
        if collide(maincar, policecar):
            maincar.life -= 1
            policecar.y = 1000
        if collide(maincar, heart):
            heart.y = 10000
            maincar.life += 1

    for Box in boxes:
        if collide(policecar, Box):
            Box.y = 900
    for Box in boxes:
        if collide(heart, Box):
            Box.y = 900

    scoretime += 1 * boostspeed # 스코어
    score = int(scoretime / 400)



def exit():
    global maincar, policecar, road1, road2, hearts, boxes, item, itemview, scorescreen, heart

    del(maincar)
    del(policecar)
    del(road1)
    del(road2)
    del(item)
    del(boxes)
    del(hearts)
    del(heart)
    del(itemview)
    del(scorescreen)

    f = open('data_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    score_data.append({"Score": score})
    print(score_data)

    f = open('data_file.txt', 'w')
    json.dump(score_data, f)
    f.close()


def draw(frame_time):

    clear_canvas()
    scorescreen.draw()

    road1.draw()
    road2.draw()
    maincar.draw()
    policecar.draw()
    item.draw()
    itemview.draw()
    hearts.draw()
    heart.draw()

    for Box in boxes:
        Box.draw()

    font.draw(600, 550, 'SCORE :%3d' % score, (255, 255, 255))
    font.draw(700, 450, 'X %3d' % maincar.life, (255, 255, 255))
    font.draw(700, 350, 'X %3d' % itemcount, (255, 255, 255))
    update_canvas()


