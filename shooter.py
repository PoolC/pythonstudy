#!/usr/bin/env python
#coding:utf-8

# 모듈 로딩
import os
import pygame
from pygame.locals import *
from pygame.compat import geterror
import math

if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

def main():
    # 모/든/것/을 초기화
    pygame.init()
    screen = pygame.display.set_mode((480, 640))
    pygame.display.set_caption('막장 슈팅 게임')
    pygame.mouse.set_visible(1)
    
    # 배경 이미지 만들기
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    from gameobject.player import Player
    from gameobject.enemy import Enemy
    from manager.collision import CollisionManager
    from manager.enemy import EnemySpawner
    
    # 오브젝트 준비
    clock = pygame.time.Clock()
    player = Player() # 플레이어
    #enemy = Enemy((50, 100)) # 테스트 적기
    
    playergroup = pygame.sprite.RenderPlain((player,))
    #enemygroup = pygame.sprite.RenderPlain((enemy,))
    enemygroup = pygame.sprite.RenderPlain()
    
    player.pellets = playergroup
    
    # 매니저 준비
    collisionmanager = CollisionManager(playergroup, enemygroup)
    enemyspawner = EnemySpawner(enemygroup)
    
    #Main Loop
    going = True
    while going:
        clock.tick(60)

        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False
            elif event.type == MOUSEBUTTONDOWN:
                player.fire()
            elif event.type == MOUSEBUTTONUP:
                #fist.unpunch()
                pass

        # 모/든/것/을 업데이트한다.
        playergroup.update()
        enemygroup.update()
        collisionmanager.update()
        enemyspawner.update()
        
        # 모/든/것/을 그린다
        screen.blit(background, (0, 0))
        playergroup.draw(screen)
        enemygroup.draw(screen)
        
        pygame.display.flip()

    pygame.quit()

    
if __name__ == '__main__':
    main()
