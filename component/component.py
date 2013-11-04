#coding:utf-8

class Component(object):
    def __init__(self, world):
        self.world = world
        
    def send(self, receiver, msg, msgargs):
        if hasattr(receiver, 'handle'):
            receiver.handle(self, msg, msgargs)
