import pygame as pg
import numpy as np
import numba as nb
import time
import sys

screen = pg.display.set_mode((1300, 900), pg.DOUBLEBUF, pg.OPENGL)
pg.display.set_caption("My Game")

clock = pg.time.Clock()
running = True
fps = 165
objects = []
objColors = []

objects.append(pg.Rect(0, 0, 100, 100))
objColors.append((255, 255, 255))

while running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            running = False

    screen.fill((0, 0, 30))
    for i in range(len(objects)):
        pg.draw.rect(screen, objColors[i], objects[i])
    pg.display.flip()

pg.quit()
sys.exit()
