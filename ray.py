import pygame as pg

from settings import *

class Ray():
    def __init__(self, x, y, dirX, dirY):
        self.x = x
        self.y = y
        self.dirX = dirX
        self.dirY = dirY

    def draw(self, screen):
        pg.draw.line(screen, WHITE, (self.x, self.y), (self.x + 10 * self.dirX, self.y + 10 * self.dirY))