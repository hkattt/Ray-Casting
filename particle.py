import pygame as pg
import math

from ray import Ray
from settings import *

class Particle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rays = []
        for angle in range(0, 360, 10):
            ray = Ray(self.x, self.y, math.radians(angle))
            self.rays.append(ray)

    def draw(self, screen, walls):
        pg.draw.circle(screen, WHITE, (self.x, self.y), 10)
        for ray in self.rays:
            closest = float('inf')
            closest_point = None
            for wall in walls:
                p = ray.intersects(wall)
                if p != None:
                    distance = math.dist((ray.x, ray.y), p)
                    if distance < closest:
                        closest = distance
                        closest_point = p
            if closest_point != None:
                pg.draw.line(screen, WHITE, (ray.x, ray.y), closest_point)

    def update(self):
        dX, dY = pg.mouse.get_pos()
        self.x, self.y = dX, dY

        for ray in self.rays:
            ray.x, ray.y = dX, dY       

