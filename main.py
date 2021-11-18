import pygame as pg
import numpy as np
import random
import math

from particle import Particle
from wall import Wall
from button import Button
from settings import *

pg.init()

running = True;

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

pg.display.set_caption("Ray Casting")

particle = Particle(WIDTH / 4, HEIGHT / 2)
walls = []
button = Button(RED, WIDTH - 75, HEIGHT - 50, 100, 50, "New Walls", 15)

def gen_walls():
    """ Generates 5 random walls within the left window """
    global walls
    walls = []
    for _ in range(5):
        x1, y1 = random.randint(0, WIDTH / 2), random.randint(0, HEIGHT)
        x2, y2 = random.randint(0, WIDTH / 2), random.randint(0, HEIGHT)
        wall = Wall(x1, y1, x2, y2)
        walls.append(wall)

def render_walls():
    """ Renders walls based on ray information from the particle"""
    rect_width = (WIDTH / 2) / len(particle.rays)
    for i in range(0, len(particle.rays)):
        ray = particle.rays[i]
        closest_point = ray.closest_wall(walls)

        # Current say does not hit a wall (black spot)
        if closest_point == None: 
            continue

        distance = math.dist((ray.x, ray.y), closest_point)

        # Calculates the colour and height of the rectangle
        colour = 255 - np.interp(distance, [0, WIDTH / 2], [0, 255]) 
        height = HEIGHT - np.interp(distance, [0, WIDTH / 2], [0, HEIGHT])

        # Draws the rectangle
        pg.draw.rect(screen, 
                    (colour, colour, colour), 
                    ((WIDTH / 2) + i * rect_width, 
                    (HEIGHT / 2) - (height / 2), 
                    rect_width + 1, 
                    height))
        
def update():
    """ Updates the particle and button """
    particle.update()
    button.update()

def events():
    """ Checks for and handle events """
    global running
    
    keys = pg.key.get_pressed()
    # Handles rotation
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        particle.rotate(0.1)
    elif keys[pg.K_LEFT] or keys[pg.K_a]:
        particle.rotate(-0.1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        if event.type == pg.MOUSEBUTTONUP:
            dX, dY = pg.mouse.get_pos()
            if button.mouse_over((dX, dY)):
                gen_walls()        
            
def paint():
    """ Draws objects onto the screen """
    screen.fill(BLACK) 
    pg.draw.line(screen, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    particle.draw(screen, walls)
    for wall in walls:
        wall.draw(screen)
    render_walls()
    button.draw(screen)
    pg.display.update()

def run():
    """ Main 'game' loop """
    while running:
        clock.tick(FPS)
        update()
        events()
        paint()        

if __name__ == "__main__":
    gen_walls()
    run()
