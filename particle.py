import pygame as pg
import math

from ray import Ray
from settings import *

class Particle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rays = []
        for angle in range(0, 75, 1):
            ray = Ray(self.x, self.y, math.radians(angle))
            self.rays.append(ray)

    def draw(self, screen, walls):
        """ Draws the particle onto the screen """
        # Draws a circle representation of the particle
        pg.draw.circle(screen, RED, (self.x, self.y), 10)

        # Draws lines which intersect with the walls
        for i in range(0, len(self.rays), 2):
            ray = self.rays[i]
            closest_point = ray.closest_wall(walls)
            if closest_point != None:
                pg.draw.line(screen, RED, (ray.x, ray.y), closest_point)

    def rotate(self, angle):
        """ Rotates the particle (clockwise) by the given angle """
        for ray in self.rays:
            x, y = ray.dirX, ray.dirY
            ray.dirX = x * math.cos(angle) - (y * math.sin(angle))
            ray.dirY = x * math.sin(angle) + (y * math.cos(angle))             

    def update(self):
        """ Updates the position of the particle based on the position of the mouse"""
        dX, dY = pg.mouse.get_pos()

        if (dX <= WIDTH / 2):
            self.x, self.y = dX, dY

            for ray in self.rays:
                ray.x, ray.y = dX, dY       

