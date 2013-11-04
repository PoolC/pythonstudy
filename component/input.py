#coding:utf-8

@component()
class InputComponent(Component):
    def __init__(self):
        Component.__init__(self)
        
    def tick(self):
        print '%s{%d} ticks!' % (self.__class__.__name__, id(self))
        
    def _handle_repeat(self, sender, msgargs):
        print 'handle repeat called with arguments: ' + str(msgargs)
