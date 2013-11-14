#coding:utf-8
from utility import component, Component
import pygame
import os
import locale
from pygame.locals import *
from pygame.compat import geterror
import __main__

main_dir = os.path.split(os.path.abspath(__main__.__file__))[0]
data_dir = os.path.join(main_dir, 'data')
system_encoding = locale.getpreferredencoding()

# 이미지 리소스 로딩하기
def load_image(name, colorkey=None):
    fullname = unicode(os.path.join(data_dir, name).decode(system_encoding))
    try:
        f = open(fullname, 'rb')
        content = f.read()
        f.seek(0)
        image = pygame.image.load(f, fullname.encode('utf-8'))
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class PygameSprite(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(filename, -1)
        self.rect = self.image.get_rect()

@component()
class SpriteComponent(Component):
    def __init__(self, filename, display):
        Component.__init__(self)
        self.sprite = PygameSprite(filename)
        self._display = display
        
    def _handle_sprite_teleport_x(self, sender, msgargs):
        x = msgargs
        cam_pos = self.sendto(self._display, 'cam_pos')
        self.sprite.rect.midbottom = (x - cam_pos[0], self.sprite.rect.midbottom[1])
        
    def _handle_sprite_teleport_y(self, sender, msgargs):
        y = msgargs
        cam_pos = self.sendto(self._display, 'cam_pos')
        self.sprite.rect.midbottom = (self.sprite.rect.midbottom[0], y - cam_pos[1])
        
    def tick(self):
        pass
