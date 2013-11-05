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
        
    def _handle_sprite_name(self, sender, msgargs):
        return self._sprite_name
        
    def tick(self):
        pass
