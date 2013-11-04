#coding:utf-8
from utility import component, Component

@component()
class CameraComponent(Component):
    def __init__(self):
        Component.__init__(self)
        
    def tick(self):
        pass
