import pygame
import sys
import os
from player import Player
from enemy import Enemy
from missile import Missile
pygame.init()
pygame.font.init()
width = 600
height = 400
level = 1
run = False
font = pygame.font.SysFont("Comic Sans MS", 30)
scorefont = pygame.font.SysFont("Comic Sans MS", 20)
score = 0
scoretext = scorefont.render("Score: {}".format(score), True, (255, 255, 255))
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Wars (By Zoxy)')
background = pygame.image.load(os.path.join("imgs", "background.png")).convert_alpha()
time = pygame.time.Clock()

def Game():
    global level
    run = True
    player = Player(width / 2, height - 50, level * 20)
    win.fill((0, 0, 0))
    enemies = []
    missiles = []
    global score
    score = 0
    for i in range(level * 5):
        enemies.append(Enemy(width / 2, 0))
    while True:
        if run:
            time.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.bullets > 0:
                        player.bullets -= 1
                        missiles.append(Missile(player.rect.x, player.rect.y))
                    
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.MoveToLeft()
            if keys[pygame.K_RIGHT]:
                player.MoveToRight()
            
            for i in enemies:
                if iscollide(player, i):
                    run = False
                for j in missiles:
                    if iscollide(j, i) and i.rect.y > 0:
                        score += 1
                        enemies.remove(i)
                        missiles.remove(j)
            win.fill((0, 0, 0))
            win.blit(background, [0, 0])
            win.blit(player.img, [player.rect.x, player.rect.y])
            for i in enemies:
                i.MoveEnemy()
                win.blit(i.img, [i.rect.x, i.rect.y])
            for i in missiles:
                i.MoveMissile()
                win.blit(i.img, [i.rect.x, i.rect.y])
                if i.rect.y < 0:
                    missiles.remove(i)
            if len(enemies) <= 0:
                level += 1
                run = False
            scoretext = scorefont.render("Score: {}".format(score), True, (255, 255, 255))
            bullettext = scorefont.render("Bullets: {}".format(player.bullets), True, (255, 255, 255))
            leveltext = scorefont.render("Level: {}".format(level), True, (255, 255, 255))
            win.blit(scoretext, (width - 100, height - 50))
            win.blit(bullettext, (width - 100, height - 70))
            win.blit(leveltext, (width - 100, height - 90))
            pygame.display.update()
            time.tick(60)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        run = True
            if run == True:
                Game()
                break
            if len(enemies) <= 0:
                text = font.render('You Win!', True, (255, 255, 255))
            else:
                text = font.render('You Lose!', True, (255, 255, 255))
            win.blit(text, (width / 2 - 50, height / 2 - 20))
            pygame.display.update()
            
    
def iscollide(sprite1, sprite2):
    if pygame.sprite.collide_rect(sprite1, sprite2):
        return True
    return False

Game()

