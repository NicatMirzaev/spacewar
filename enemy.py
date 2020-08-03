import pygame
import random
import os
class Enemy(object):
    def __init__(self, x, y):
        self.img = pygame.image.load(os.path.join("imgs", "enemy.png")).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = random.randrange(-10, 10)
        self.speedy = random.randrange(5, 15)
    def MoveEnemy(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.x < 0:
            self.speedx += 10
            self.rect.x += random.randint(1, 7)
        if self.rect.x + self.img.get_width() > 600:
            self.speedx -= 10
            self.rect.x -= random.randint(1, 7)
        if self.rect.y > 400:
            self.rect.x = 330
            self.rect.y = -10
            self.speedx = random.randrange(-25, 25)
            self.speedy = random.randrange(8, 20)
