#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

cols = int(input('Cols? '))
rows = int(input('Rows? '))

WIDTH, HEIGHT = 600, 400
g2d.init_canvas((WIDTH, HEIGHT))

w, h = WIDTH / cols, HEIGHT / rows
delta_blue, delta_green = 0, 0
if cols > 1:
    delta_blue = 255.0 / (cols - 1)
if rows > 1:
    delta_green = 255.0 / (rows - 1)

for y in range(rows):
    for x in range(cols):
        color = 0, int(delta_green * y), int(delta_blue * x)
        rect = int(w * x), int(h * y), int(w - 1), int(h - 1)
        g2d.draw_rect(color, rect)

g2d.main_loop()
