import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from brick import Brick

name = "MainState"

boy = None
grass = None
balls = []
brick = None

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True




def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global balls
    balls = [Ball() for i in range(200)]
    game_world.add_objects(balls, 1)

    global brick
    brick = Brick()
    game_world.add_object(brick, 1)



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for ball in balls.copy():
        if collide(ball, grass):
            ball.stop()
        if collide(ball, boy):  # 1차 적으로 볼과 소년의 충돌
            balls.remove(ball)  # 일단 충돌이 없어지면, 충돌체크가 더 이상 필요하지 않기 때문에
            game_world.remove_object(ball)
            
        # 벽돌이랑 부딫힐경우
        if collide(ball, brick):
            if ball.on == False:
                ball.stop()
                ball.on_x = ball.x - brick.x
                ball.on_y = ball.y - brick.y
                ball.on = True
                ball.target = brick

        # 같은 축구공 끼리 부딪힐 경우
        for col_ball in balls:
            if ball != col_ball and collide(ball, col_ball):
                if col_ball.on and ball.on == False:
                    ball.stop()
                    ball.on_x = ball.x - col_ball.x
                    ball.on_y = ball.y - col_ball.y
                    ball.on = True
                    ball.target = col_ball


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






