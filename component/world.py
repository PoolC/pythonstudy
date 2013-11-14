#coding:utf-8
import os
from utility import component, Component, QuitRequestFromFrontend
import __main__

main_dir = os.path.split(os.path.abspath(__main__.__file__))[0]
data_dir = os.path.join(main_dir, 'data')

@component()
class WorldComponent(Component):
    def __init__(self, mapfilename):
        Component.__init__(self)
        self._entities = {}
        self._frontend = None
        self._camera = None
        self._tile_width = 40
        self._tile_height = 40
        self._player = None

        name = os.path.join(data_dir, mapfilename)
        try:
            with open(name) as f:
                self._mapdata = [[int(xxx) for xxx in xx.split()] for xx in f.read().split('\n')]
        except IOError:
            print '[Error] Map file %s loading failure.' % name
            self._mapdata = None
        
    def _handle_spawn_me(self, sender, msgargs):
        print '{%d} tries to spawn in the world. It\'s name is %s.' % (id(sender), self.sendto(sender, 'name'))
        if id(sender) in self._entities:
            raise Exception('DuplicatedSpawnWarning')
        else:
            self._entities[id(sender)] = sender
            print 'Spawn completed at %s.' % str(self.sendto(sender, 'pos'))
            
            if self._frontend:
                self.sendto(self._frontend, 'spawn', sender)
                
    def _handle_i_am_player(self, sender, msgargs):
        self._player = sender
        print 'Player set to', id(self._player)
        
    def _handle_move_player(self, sender, msgargs):
        if self._player:
            print 'Player will move by', msgargs
            self.sendto(self._player, 'move', msgargs)
        
    def _handle_set_frontend(self, sender, msgargs):
        self._frontend = sender
        self.sendto(sender, 'set_world')
        self.sendto(sender, 'map_data', self._mapdata)
        
    def _handle_set_camera(self, sender, msgargs):
        pass
        
    def _handle_quit(self, sender, msgargs):
        if sender == self._frontend:
            raise QuitRequestFromFrontend()
            
    def _find_floor(self, pos):
        posx, posy = pos
        tilex = int(posx//self._tile_width)
        tiley = int(posy//self._tile_height)
        
        # Sweep up if the current tile is not empty, sweep down otherwise.
        if self._mapdata[tiley][tilex] == 0:
            for ty in range(tiley, len(self._mapdata)):
                if self._mapdata[ty][tilex] != 0:
                    return ty*self._tile_height
        else:
            for ty in range(tiley, 0, -1):
                if self._mapdata[ty-1][tilex] == 0:
                    return ty*self._tile_height
        
        raise Exception
        
    def tick(self):
        for entity_id, entity in self._entities.iteritems():
            self.sendto(entity, 'floor', self._find_floor(self.sendto(entity, 'pos')))
