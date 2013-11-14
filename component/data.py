#coding:utf-8
from utility import component, Component

@component()
class DataComponent(Component):
    def __init__(self, name, pos, sprite_name):
        Component.__init__(self)
        self._name = name
        self._pos = pos
        self._sprite_name = sprite_name

    def _handle_name(self, sender, msgargs):
        return self._name
        
    def _handle_pos(self, sender, msgargs):
        return self._pos
        
    def _handle_set_pos(self, sender, msgargs):
        self._pos = msgargs
        self.sendto(self.channel, 'sprite_teleport_y', self._pos[1])
        
    def _handle_move(self, sender, msgargs):
        dx, dy = msgargs
        self._pos = (self._pos[0] + dx, self._pos[1] + dy)
        print id(self.channel), 'moved to', self._pos
        self.sendto(self.channel, 'sprite_teleport_x', self._pos[0])
        self.sendto(self.channel, 'sprite_teleport_y', self._pos[1])
        
    def _handle_sprite_name(self, sender, msgargs):
        return self._sprite_name
        
    def _handle_teleport_y(self, sender, msgargs):
        y = msgargs
        
        self._pos = (self._pos[0], y)
        
        self.sendto(self.channel, 'sprite_teleport_y', y)
        
    def tick(self):
        pass
