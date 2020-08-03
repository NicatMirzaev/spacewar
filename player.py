import pygame
import os
class Player(object):
    def __init__(self, x, y, bullets):
        self.img = pygame.image.load(os.path.join("imgs", "player.png")).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bullets = bullets
    def MoveToLeft(self):
        self.rect.x -= 5
        if self.rect.x < 0:
            self.rect.x = 0
        
    def MoveToRight(self):
        self.rect.x += 5
        if self.rect.x + self.img.get_width() > 600:
            self.rect.x = self.rect.x - self.img.get_width()

