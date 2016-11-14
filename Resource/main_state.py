import random
import json
import os

from pico2d import *
from maincar import Maincar
from policecar import Policecar
from road import Road
from item import Item
from box import Box
from heart import Heart

import game_framework
import title_state



name = "MainState"

leftmove = 0
rightmove = 0
upmove = 0
downmove = 0
score = 0
boxnum = 2

def enter():
    global maincar, policecar, road1, road2, font, boxes, item, hearts
    maincar = Maincar()
    policecar = Policecar()
    road1 = Road()
    road2 = Road()
    boxes = [Box() for i in range(boxnum)]
    item = Item()
    hearts = [Heart()for i in range(maincar.life)]
    road2.y = 800

    font = load_font('ENCR10B.TTF')
    game_framework.reset_time()


def exit():
    global maincar, policecar, road1, road2, font, hearts, boxes, item

    del(maincar)
    del(policecar)
    del(road1)
    del(road2)
    del(font)
    del(item)
    del(boxes)
    del(hearts)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global leftmove, rightmove, upmove, downmove
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                leftmove = 1
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                leftmove = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                rightmove = 1
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                rightmove = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                upmove = 1
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
                upmove = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                downmove = 1
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
                downmove = 0

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def update(frame_time):
    global leftmove, rightmove, upmove, downmove, score
    road1.update()
    road2.update()
    for Box in boxes:
        Box.update()
    policecar.update()
    item.update()
    if leftmove == 1 and maincar.x > 50:
        maincar.x -= 1
    elif rightmove == 1 and maincar.x < 550:
        maincar.x += 1
    elif upmove == 1 and maincar.y < 500:
        maincar.y += 1
    elif downmove == 1 and maincar.y > 80:
        maincar.y -= 1

    if collide(maincar, item):
        downmove = 0
        upmove = 0
        rightmove = 0
        leftmove = 0

    score += 1
    print(score)

def draw(frame_time):

    clear_canvas()
    road1.draw()
    road2.draw()
    maincar.draw()
    maincar.draw_bb()
    policecar.draw()
    policecar.draw_bb()
    item.draw()
    item.draw_bb()
    for Box in boxes:
        Box.draw()
        Box.draw_bb()
    for Heart in hearts:
        Heart.draw()
    update_canvas()


