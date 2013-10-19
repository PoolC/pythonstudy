#coding:utf-8
import pygame
from utility import load_image
from pellet import Pellet

# 플레이어
class Player(pygame.sprite.Sprite):
    """좌우키를 눌러서 이동시킬 수 있는 플레이어의 비행기"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('player.png', -1)

    def update(self):
        "좌우키 눌러서 이동, CTRL키로 총알 발사"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos

    def fire(self):
        self.pellets.add(Pellet(self.rect.midtop))
