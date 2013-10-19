#coding:utf-8
import os
import pygame
from pygame.locals import *
from pygame.compat import geterror
import __main__
import json

main_dir = os.path.split(os.path.abspath(__main__.__file__))[0]
data_dir = os.path.join(main_dir, 'data')

# 이미지 리소스 로딩하기
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_json(name):
    fullname = os.path.join(data_dir, name)
    try:
        return json.loads(open(fullname).read())
    except:
        print ('JSON 파일 로딩 실패:', fullname)
        raise SystemExit(str(geterror()))
