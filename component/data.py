#coding:utf-8
from utility import component, Component

@component()
class DataComponent(Component):
    def __init__(self, name, pos):
        Component.__init__(self)
        self._name = name
        self._pos = pos

    def _handle_name(self, sender, msgargs):
        return self._name
        
    def _handle_pos(self, sender, msgargs):
        return self._pos
        
    def tick(self):
        pass
