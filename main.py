import pygame as pg
import random

from particle import Particle
from wall import Wall
from settings import *

pg.init()

running = True;

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

pg.display.set_caption("Ray Casting")

particle = Particle(WIDTH / 2, HEIGHT / 2)
walls = []

def gen_walls():
    for _ in range(5):
        x1, y1 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        x2, y2 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        wall = Wall(x1, y1, x2, y2)
        walls.append(wall)

def update():
    particle.update()

def events():
    global running
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

def paint():
    screen.fill(BLACK)
    particle.draw(screen, walls)
    for wall in walls:
        wall.draw(screen)
    pg.display.update()

def run():
    while running:
        clock.tick(FPS)
        update()
        events()
        paint()

gen_walls()
run()
