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
        background.fill((10, 20, 30))
        
        self._screen = screen
        self._background = background
        self._world = None
        self._default_render_group = pygame.sprite.RenderPlain()
        
        self._tile_width = 40
        self._tile_height = 40
        self._camera_pos = (0, self._tile_height*4)
        
        self._leftkey = False
        self._rightkey = False
        
    def _handle_set_world(self, sender, msgargs):
        self._world = sender
        
    def _handle_cam_pos(self, sender, msgargs):
        return self._camera_pos
        
    def _handle_spawn(self, sender, msgargs):
        entity = msgargs
        
        # Create a sprite component for 'entity'
        sprite = SpriteComponent(self.sendto(entity, 'sprite_name'), self.channel)
        
        # Attach it to 'entity'
        self.sendto(entity, 'attach', sprite)
        
        # Get the position of 'entity'
        pos = self.sendto(entity, 'pos')
        
        # Move the sprite to the position 'pos'
        sprite.sprite.rect.midbottom = (pos[0] - self._camera_pos[0], pos[1] - self._camera_pos[1])
        
        # Register the pygame sprite object to the default render group
        self._default_render_group.add(sprite.sprite)
        
    def _handle_map_data(self, sender, msgargs):
        mapdata = msgargs
        
        self._map_rows = len(mapdata)
        self._map_cols = len(mapdata[0])
        
        entitysurface = pygame.Surface((self._tile_width*self._map_cols, self._tile_height*self._map_rows))
        self._entitysurface = entitysurface
        
        mapsurface = pygame.Surface((self._tile_width*self._map_cols, self._tile_height*self._map_rows))
        mapsurface = mapsurface.convert()
        mapsurface.fill((0, 0, 0))
        
        EMPTY = (10, 20, 30)
        GROUND = (0,255,0)
        SMOKESTACK = (100,100,100)
        FINISH = (255,255,255)
        colors = [EMPTY, GROUND, SMOKESTACK, FINISH]
        
        for i, r in enumerate(mapdata):
            for j, c in enumerate(r):
                pygame.draw.rect(mapsurface, colors[c], (self._tile_width*j, self._tile_height*i, self._tile_width, self._tile_height))

        self._mapsurface = mapsurface
        
    def tick(self):
        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                self.sendto(self._world, 'quit')
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                self.sendto(self._world, 'quit')
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self._rightkey = True
                elif event.key == K_LEFT:
                    self._leftkey = True
            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    self._rightkey = False
                elif event.key == K_LEFT:
                    self._leftkey = False
            
        # Draw everything
        self._screen.blit(self._background, (0, 0))
        self._screen.blit(self._mapsurface, (-self._camera_pos[0], -self._camera_pos[1]))
        self._default_render_group.draw(self._screen)
        
        player_move_speed = 0.25
        if self._rightkey and not self._leftkey:
            self.sendto(self._world, 'move_player', (player_move_speed, 0))
        elif not self._rightkey and self._leftkey:
            self.sendto(self._world, 'move_player', (-player_move_speed, 0))
        
        pygame.display.flip()
