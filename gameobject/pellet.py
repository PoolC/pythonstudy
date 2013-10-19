#coding:utf-8
import pygame
from utility import load_image

# 총알 총알
class Pellet(pygame.sprite.Sprite):
    """앞으로 전진하는 총알"""
    image = pygame.Surface((10,10))
    image = image.convert()
    image.fill((255, 255, 255))

    def __init__(self, spawnpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = Pellet.image
        self.rect = self.image.get_rect()
        self.hp = 1
        
        # 초기 위치 설정
        self.rect.midtop = spawnpos
        
    def update(self):
        #self.rect.midtop = (self.rect.midtop[0], self.rect.midtop[1]-1)
        self.rect.move_ip(0,-10)
        if self.rect.midtop[1] < 10:
            self.kill()
        