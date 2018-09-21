# -*- coding: utf-8 -*-

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, i):
        self.stack.append(i)
    def pop(self):
        return self.stack.pop()
    def isempty(self):
        return self.stack == []
    def peek(self):
        return self.stack[len(self.stack) - 1]
    def __str__(self):
        return str(self.stack)