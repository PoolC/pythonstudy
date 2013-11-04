#coding:utf-8
from utility import component, Component, QuitRequestFromFrontend

@component()
class WorldComponent(Component):
    def __init__(self):
        Component.__init__(self)
        self._entities = {}
        self._frontend = None
        self._camera = None
        
    def _handle_spawn_me(self, sender, msgargs):
        print '{%d} tries to spawn in the world. It\'s name is %s.' % (id(sender), self.sendto(sender, 'name'))
        if id(sender) in self._entities:
            raise Exception('DuplicatedSpawnWarning')
        else:
            self._entities[id(sender)] = sender
            print 'Spawn completed at %s.' % str(self.sendto(sender, 'pos'))
            
    def _handle_set_frontend(self, sender, msgargs):
        self._frontend = sender
        self.sendto(sender, 'set_world')
        
    def _handle_set_camera(self, sender, msgargs):
        pass
        
    def _handle_quit(self, sender, msgargs):
        if sender == self._frontend:
            raise QuitRequestFromFrontend()
        
    def tick(self):
        pass
