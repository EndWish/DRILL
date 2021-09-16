from pico2d import *

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

import math

x = 400
y = 90
d = 0

while(1):
    x = 400
    y = 90
    d = 0
    #사각형
    while (1):
        if(d == 0):
            x += 3
            if(x > 750):
                d = 90
                
        elif d == 90:
            y += 3
            if(y > 510):
                d = 180
            
        elif d == 180:
            x -= 3
            if(x < 50):
                d = 270
            
        elif d == 270:
            y -= 3
            if(y < 90):
                d = 0
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        if(d == 0 and 397 <= x and x < 400):
            break;

    #원
    d = -90
    while (1):
        d += 1
        x = math.cos(d/360*2*math.pi) * 210
        y = math.sin(d/360*2*math.pi) * 210
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400 + x, 300 + y)
        if(d == 270):
            break;

close_canvas()
