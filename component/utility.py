#coding:utf-8

component_classes = []

class component(object):
    def __call__(self, target):
        global component_classes
        component_classes.append(target)
        setattr(target, '_instances', [])
        return target

class Component(object):
    def __init__(self):
        self._instances.append(self)
        self._nextcomp = None
        self.channel = None
        
    def sendto(self, receiver, msg, msgargs = None):
        return self.channel.sendto(receiver, msg, msgargs)

def tickall():
    for compcls in component_classes:
        for comp in compcls._instances:
            comp.tick()

class QuitRequestFromFrontend(Exception):
    pass
