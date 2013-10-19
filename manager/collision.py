import pygame
import pygame.sprite

class CollisionManager(object):

    def __init__(self, playergroup, enemygroup):
        self.playergroup = playergroup
        self.enemygroup = enemygroup

    def getenemyhitbyplayer(self):
        return pygame.sprite.groupcollide(self.enemygroup, self.playergroup, False, False)
        
    def update(self):
        for enemy, player in self.getenemyhitbyplayer().iteritems():
            #print enemy, player
            for p in player:
                enemy.hp -= 1
                p.hp -= 1
                
                if p.hp <= 0:
                    p.kill()
                    
                if enemy.hp <= 0:
                    enemy.kill()
                    break