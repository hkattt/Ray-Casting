import pygame as pg
import math

from settings import *

class Ray():
    def __init__(self, x, y, dirX, dirY):
        self.x = x
        self.y = y
        self.dirX = dirX
        self.dirY = dirY

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.dirX = math.cos(angle)
        self.dirY = math.sin(angle)

    def intersects(self, wall):
        x1, y1 = wall.x1, wall.y1
        x2, y2 = wall.x2, wall.y2
        x3, y3 = self.x, self.y
        x4, y4 = self.x + self.dirX, self.y + self.dirY

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if den == 0:
            return
        
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if (0 < t and t < 1 and u > 0):
            intersectX = x1 + t * (x2 - x1)
            intersectY = y1 + t * (y2 - y1)
            return (intersectX, intersectY)
        return

    def draw(self, screen):
        pg.draw.line(screen, WHITE, (self.x, self.y), (self.x + 10 * self.dirX, self.y + 10 * self.dirY))