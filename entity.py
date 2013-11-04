#coding:utf-8
import types

class Channel(object):
    def __init__(self, owner):
        self._owner = owner

    def _process_message(self, sender, msg, msgargs):
        return self._owner._handle(sender, msg, msgargs)
        
    def sendto(self, receiver, msg, msgargs = None):
        return receiver._process_message(self, msg, msgargs)

class Entity(object):
    def __init__(self):
        self.channel = Channel(self)
        self._nextcomp = None
        self._children = []
        
    def attach(self, comp):
        assert comp._nextcomp is None
        
        c = self
        while c._nextcomp is not None:
            c = c._nextcomp
        c._nextcomp = comp
        comp.channel = self.channel
        
        return self
        
    def components(self):
        c = self
        while c._nextcomp is not None:
            yield c._nextcomp
            c = c._nextcomp
            
    def add(self, entity):
        self._children.append(entity)
        
    def _handle(self, sender, msg, msgargs):
        c = self
        while c._nextcomp is not None:
            c = c._nextcomp
            try:
                handler = getattr(c, '_handle_' + msg)
            except AttributeError:
                handler = None
            if handler:
                return handler(sender, msgargs)

        return None

    
def tick(compcls):
    for comp in compcls.instances:
        comp.tick()

def tickall():
    for compcls in component_classes:
        tick(compcls)

def send(sender, receiver, msg, msgargs):
    receiver.send(sender, msg, msgargs)
