#coding:utf-8
from utility import component, Component
import pygame
from pygame.locals import *

@component()
class DisplayComponent(Component):
    def __init__(self):
        Component.__init__(self)
        
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('CBES Mario')
        pygame.mouse.set_visible(1)
        
        # background surface initialization
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((10, 200, 30))
        
        self._screen = screen
        self._background = background
        self._world = None
        
    def _handle_set_world(self, sender, msgargs):
        self._world = sender
        
    def tick(self):
        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                self.sendto(self._world, 'quit')
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                self.sendto(self._world, 'quit')
                
        # Draw everything
        self._screen.blit(self._background, (0, 0))
        pygame.display.flip()
