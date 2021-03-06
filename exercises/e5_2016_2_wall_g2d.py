#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from random import choice, randrange
from actor import Actor, Arena

class Ball(Actor):
    W, H = 20, 20
    SPEED = 5

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = self.SPEED, self.SPEED
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        if not (0 <= self._x + self._dx <= arena_w - self.W):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= arena_h - self.H):
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def collide(self, other):
        if isinstance(other, Wall):
            bx, by, bw, bh = self.position()  # ball's pos
            wx, wy, ww, wh = other.position() # wall's pos
            borders_distance = [(wx - bw - bx, 0), (wx + ww - bx, 0),
                                (0, wy - bh - by), (0, wy + wh - by)]
            # move to the nearest border: left, right, top or bottom
            move = min(borders_distance, key=lambda m: abs(m[0] + m[1]))
            self._x += move[0]
            self._y += move[1]

    def position(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0, 0, self.W, self.H


class Wall(Actor):

    def __init__(self, arena, x, y, w, h):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 0, self._w, self._h


def update():
    arena.move_all()  # Game logic

    g2d.fill_canvas((255, 255, 255))
    for a in arena.actors():
        if isinstance(a, Wall):
            g2d.draw_rect((127, 127, 127), a.position())
        else:
            g2d.draw_image_clip(sprites, a.position(), a.symbol())

def main():
    global arena, sprites
    arena = Arena(320, 240)
    Ball(arena, 40, 80)
    Ball(arena, 85, 40)
    Wall(arena, 115, 80, 100, 20)

    g2d.init_canvas(arena.size())
    sprites = g2d.load_image("sprites.png")

    g2d.main_loop(update, 1000 // 30)  # millis

main()
