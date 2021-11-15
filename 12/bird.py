import random

import game_framework
from pico2d import *
from ball import Ball

import game_world

# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 100.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
# 10픽셀은 30cm이며 , 새의 속도는 100km/h 이다.

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14
# 초당 2번의 이미지변환(애니매이션 변환)이 이루어지며 총14가지 이미지를 순환한다.

# Bird Size
BIRDS_SIZE_METER = 1.0
BIRDS_SIZE_PIXEL = BIRDS_SIZE_METER * PIXEL_PER_METER
# 새의 크기는 1m로 설정 했으며, 새의 pixel 크기 = BIRDS_SIZE_METER * PIXEL_PER_METER 이다
# 참고로 사람의 크기가 3m 정도 된다. 그래서 1m인 새가 사람보다 작아보임

class Bird:
    def __init__(self):
        self.x, self.y = random.randint(0, 1600), random.randint(90, 600)
        self.image = load_image('bird100x100x14.png')
        self.dir = (-1, 1)[random.randint(0,1)]
        self.velocity = 0
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time

        # 좌우 반전
        if self.x <= 0:
            self.dir = 1
        elif 1600 <= self.x:
            self.dir = -1
            
            

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, '', self.x, self.y, BIRDS_SIZE_PIXEL, BIRDS_SIZE_PIXEL)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, 'h', self.x, self.y, BIRDS_SIZE_PIXEL, BIRDS_SIZE_PIXEL)


