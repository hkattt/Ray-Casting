import pygame as pg

from settings import *

class Wall():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, screen):
        """ Draws the wall onto the screen """
        pg.draw.line(screen, WHITE,(self.x1, self.y1), (self.x2, self.y2))