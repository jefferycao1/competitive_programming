# -*- coding: utf-8 -*-

class queue():
    def __init__(self):
        self.queue = []
    
    def add(self, i):
        self.queue.append(i)
        
    def dequeue(self):
        if (len(self.queue) >= 1):
            return self.queue.pop(0)
        else:
            raise ValueError 
    
    def peek(self):
        if (len(self.queue) >= 1):
            return self.queue[0]
        else:
            raise ValueError
    
    def isEmpty(self):
        return self.queue == []

    def __str__(self):
        return str(self.queue)
