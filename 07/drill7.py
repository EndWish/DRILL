from pico2d import *
import math

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global target_x, target_y
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            target_x, target_y = event.x, KPU_HEIGHT - 1 - event.y


def move():
    global target_x, target_y
    global x, y
    speed = 0.05

    x = target_x * speed + x * (1 - speed)
    y = target_y * speed + y * (1 - speed)


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
target_x, target_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0

hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(target_x, target_y)
    if x < target_x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    move()
    handle_events()

    delay(0.01)

close_canvas()