#coding:utf-8
from utility import component, Component

@component()
class FallComponent(Component):
    def __init__(self):
        Component.__init__(self)
        self._floor = None

    def _handle_floor(self, sender, msgargs):
        floor = msgargs
        self._floor = floor
        
        pos = self.sendto(self.channel, 'pos')
        posydiff = - (pos[1] - self._floor) / 1.0
            
        self.sendto(self.channel, 'set_pos', (pos[0], pos[1] + posydiff))
        
        # self.sendto(self.channel, 'teleport_y', floor)
        
    def tick(self):
        pass
