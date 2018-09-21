# -*- coding: utf-8 -*-
import unittest




def sortstack(stack):
    temp = Stack()
    if(len(stack.top) == 0):
        return stack
    temp.push(stack.pop())
    while (len(stack.top) != 0):
        tempnum = stack.pop()
        while(len(temp.top) > 0 and tempnum < temp.peek()):
            stack.push(temp.pop())
        temp.push(tempnum)
    
    return temp
    
    

class Stack:
    def __init__(self):
        self.top = []
        
    def __str__(self):
        return str(self.top)
    
    def push(self, i):
        self.top.append(i)
    
    def pop(self):
        if(len(self.top) == 0):
            return None
        else:
            return self.top.pop()
    
    def peek(self):
        if(len(self.top) == 0):
            return None
        else:
            return self.top[len(self.top) - 1]
        


class Test(unittest.TestCase):
    def testsort(self):
        s = Stack()
        s.push(3)
        s.push(4)
        s.push(7)
        s.push(1)
        sortedstack = sortstack(s)
        
        self.assertEqual("[1, 3, 4, 7]", str(sortedstack))

if __name__ == "__main__":
    unittest.main()
