#coding:utf-8
import pygame
from component import Component
from gameobject.utility import load_image

class SpriteCollider(Component):
    def __init__(self, world, spritename, spawnpos):
        
        Component.__init__(self, world)
        
        sprite = pygame.sprite.Sprite()
        sprite.image, sprite.rect = load_image(spritename, -1)
        sprite.rect.center = spawnpos
        self.sprite = sprite
        
        self.send(world, 'addtospritegroup', (self.sprite,))
        
    def center(self):
        return self.rect.center

    def update(self):
        pass