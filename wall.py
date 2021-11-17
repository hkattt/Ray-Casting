import pygame as pg
from extra import to_pygame

from settings import *

class Wall():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, screen):
        pg.draw.line(screen, WHITE, to_pygame((self.x1, self.y1)), to_pygame((self.x2, self.y2)))