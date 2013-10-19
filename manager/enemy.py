#coding:utf-8
import pygame
import pygame.sprite
from gameobject.utility import load_json
from gameobject.enemy import Enemy

class EnemySpawner(object):

    def __init__(self, enemygroup):
        self.enemygroup = enemygroup
        self.data = load_json('data.json')
        self.curdata = -1
        
        #self.spawnall()
        
    def spawnall(self):
        for e in self.data[self.curdata]:
            self.enemygroup.add(Enemy(coordfromindex(e)))

    def update(self):
        '''적기를 다 없앴으면 다음 스테이지로 ㄱㄱ'''
        if len(self.enemygroup) == 0:
            self.curdata += 1
            if self.curdata >= len(self.data):
                print 'MISSION ACCOMPLISHED'
                print 'RESTART'
                self.curdata = 0
                
            self.spawnall()