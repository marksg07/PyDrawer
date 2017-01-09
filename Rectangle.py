from Drawable import Drawable
from utils import between
import pygame as pg
import pygame.draw as draw
from drawer import getscreen

class Rectangle(Drawable):
    def __init__(self, x1=0, y1=0, x2=0, y2=0, border=(0,0,0), filler=(255, 255, 255), borderthick=5):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.border = border
        self.filler = filler

    def update(self, newX, newY):
        self.x2 = newX
        self.y2 = newY

    def draw(self):
        screen = getscreen()
        draw.rect(screen, border, (self.x1 - borderthick, self.y1 - borderthick, self.x2 - self.x1 + borderthick, self.y2 - self.y1 + borderthick))
        draw.rect(screen, filler, (self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1))

    def collides(self, x, y):
        return between(self.x1, x, self.x2) and between(self.y1, y, self.y2)
