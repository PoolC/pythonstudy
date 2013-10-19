#coding:utf-8
import pygame
from utility import load_image

# 적기
class Enemy(pygame.sprite.Sprite):
    """싸그리 파괴해야하는 적기"""
    def __init__(self, spawnpos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('enemy.png', -1)
        self.rect.center = spawnpos
        self.hp = 1
        
    def update(self):
        pass
        
    def fire(self):
        self.pellets.add(Pellet(self.rect.midtop))
