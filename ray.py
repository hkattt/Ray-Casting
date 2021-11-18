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
        """ Returns the point at which the ray intersects with the given wall. Returns None
            if the ray does not intersect with the wall.
            Source: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection """
        x1, y1 = wall.x1, wall.y1
        x2, y2 = wall.x2, wall.y2
        x3, y3 = self.x, self.y
        x4, y4 = self.x + self.dirX, self.y + self.dirY

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        # The wall and ray are parallel when this happens
        if den == 0:
            return
        
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if (0 < t and t < 1 and u > 0):
            intersectX = x1 + t * (x2 - x1)
            intersectY = y1 + t * (y2 - y1)
            return (intersectX, intersectY)
        return

    def closest_wall(self, walls):
        """ Returns the point of the closest intersection point. None if the 
            ray does not intersect any of the walls. """
        closest = float('inf')
        closest_point = None
        for wall in walls:
            p = self.intersects(wall)
            if p != None:
                distance = math.dist((self.x, self.y), p)
                if distance < closest:
                    closest = distance
                    closest_point = p
        return closest_point