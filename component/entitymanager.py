#coding:utf-8
from component import Component

class EntityManager(Component):
    def __init__(self, owner, playergroup, enemygroup):
        Component.__init__(self, owner)
        
        self.playergroup = playergroup
        self.enemygroup = enemygroup
        
        # All entity list
        self.entitylist = []

    def addentity(self, e):
        
        self.entitylist.append(e)
        
    def update(self):
        for e in self.entitylist:
            if hasattr(e, 'spritecollider'):
                e.spritecollider.update()
    
    def handle(self, sender, msg, msgargs):
        pass