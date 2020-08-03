import pygame
import os
class Missile(object):
    def __init__(self, x, y):
        self.img = pygame.image.load(os.path.join('imgs', 'missile.png'))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def MoveMissile(self):
        self.rect.y -= 10
        if self.rect.y < 0:
            self.rect.y = -50
           

