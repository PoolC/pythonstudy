#encoding:utf-8
from component import Component

class CollisionManager(Component):
    def __init__(self, owner):
        Component.__init__(self, owner)
