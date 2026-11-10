from pico2d import *

import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
FLIGHT_SPEED_KMPH = 20.0
FLIGHT_SPEED_MPM = (FLIGHT_SPEED_KMPH * 1000.0 / 60.0)
FLIGHT_SPEED_MPS = (FLIGHT_SPEED_MPM / 60.0)
FLIGHT_SPEED_PPS = (FLIGHT_SPEED_MPS * PIXEL_PER_METER)

FLAP_LENGTH_M = 2.0
FRAMES_PER_FLAP = 14
FLAP_FRAMES_PER_SECOND = (FLIGHT_SPEED_MPS / FLAP_LENGTH_M * FRAMES_PER_FLAP)

BIRD_FRAME_COUNT = 14
BIRD_FRAME_W = 183
BIRD_FRAME_H = 168

BIRD_HEIGHT_M = 1.5
BIRD_HEIGHT_PX = BIRD_HEIGHT_M * PIXEL_PER_METER
BIRD_WIDTH_PX = BIRD_HEIGHT_PX * BIRD_FRAME_W / BIRD_FRAME_H

FLIP_MARGIN = 100


class Bird:
    def __init__(self, x, y, dir=1):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.dir = dir
        self.frame = 0

    def update(self):
        self.frame = (self.frame +
                      FLAP_FRAMES_PER_SECOND * game_framework.frame_time) % BIRD_FRAME_COUNT
        self.x += self.dir * FLIGHT_SPEED_PPS * game_framework.frame_time
        if self.dir == 1 and self.x >= get_canvas_width() - FLIP_MARGIN:
            self.dir = -1
        elif self.dir == -1 and self.x <= FLIP_MARGIN:
            self.dir = 1

    def draw(self):
        frame = int(self.frame)
        sx = (frame % 5) * BIRD_FRAME_W
        sy = (frame // 5) * BIRD_FRAME_H
        if self.dir == 1:
            self.image.clip_draw(
                sx, sy, BIRD_FRAME_W, BIRD_FRAME_H,
                self.x, self.y, BIRD_WIDTH_PX, BIRD_HEIGHT_PX)
        else:
            self.image.clip_composite_draw(
                sx, sy, BIRD_FRAME_W, BIRD_FRAME_H,
                0, 'h', self.x, self.y, BIRD_WIDTH_PX, BIRD_HEIGHT_PX)
