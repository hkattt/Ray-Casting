import pygame as pg

from ray import Ray
from settings import *

pg.init()

WIDTH = 500
HEIGHT = 500

running = True;

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

pg.display.set_caption("Ray Casting")

ray = Ray(WIDTH / 2, HEIGHT / 2, 1, -1)

def update():
    pass

def events():
    global running
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

def paint():
    ray.draw(screen)
    pg.display.update()

def run():
    while running:
        clock.tick(FPS)
        update()
        events()
        paint()

run()
