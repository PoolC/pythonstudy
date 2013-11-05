#coding:utf-8
from sprite import SpriteComponent
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
        self._default_render_group = pygame.sprite.RenderPlain()
        
        
    def _handle_set_world(self, sender, msgargs):
        self._world = sender
        
    def _handle_spawn(self, sender, msgargs):
        entity = msgargs
        
        # Create a sprite component for 'entity'
        sprite = SpriteComponent(self.sendto(entity, 'sprite_name'))
        
        # Attach it to 'entity'
        self.sendto(entity, 'attach', sprite)
        
        # Get the position of 'entity'
        pos = self.sendto(entity, 'pos')
        
        # Move the sprite to the position 'pos'
        sprite.sprite.rect.midbottom = pos
        
        # Register the pygame sprite object to the default render group
        self._default_render_group.add(sprite.sprite)
        
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
        self._default_render_group.draw(self._screen)
        pygame.display.flip()
