import random
import json
import os

from pico2d import *
from maincar import Maincar
from policecar import Policecar
from road import Road
from item import Item
from box import Box

import game_framework
import title_state



name = "MainState"

leftmove = 0
rightmove = 0

def enter():
    global maincar, policecar, road1, road2, font, box, item
    maincar = Maincar()
    policecar = Policecar()
    road1 = Road()
    road2 = Road()
    box = Box()
    item = Item()
    road2.y = 800

    font = load_font('ENCR10B.TTF')
    game_framework.reset_time()


def exit():
    global maincar, policecar, road1, road2, font

    del(maincar)
    del(policecar)
    del(road1)
    del(road2)
    del(font)
    del(item)
    del(box)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global leftmove, rightmove
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

def update(frame_time):
    global leftmove
    road1.update()
    road2.update()
    policecar.update()
    item.update()
    if leftmove == 1:
        maincar.x -= 1
    elif rightmove == 1:
        maincar.x += 1

def draw(frame_time):

    clear_canvas()
    road1.draw()
    road2.draw()
    maincar.draw()
    policecar.draw()
    item.draw()
    box.draw()
    update_canvas()


