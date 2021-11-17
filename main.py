import pygame as pg

from ray import Ray
from wall import Wall
from extra import to_pygame
from settings import *

pg.init()

running = True;

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

pg.display.set_caption("Ray Casting")

ray = Ray(WIDTH / 2, HEIGHT / 2, 1, 0)
wall = Wall(300, 100, 300, 120)

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
    wall.draw(screen)
    p = ray.intersects(wall)
    if p != None:
        pg.draw.circle(screen, WHITE, to_pygame(p), 3)
    pg.display.update()

def run():
    while running:
        clock.tick(FPS)
        update()
        events()
        paint()

run()
