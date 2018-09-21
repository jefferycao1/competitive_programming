# -*- coding: utf-8 -*-

import unittest

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def add(self, i):
        self.stack1.append(i)
    
    def remove(self):
        if(len(self.stack1) == 0):
            return None
        self.stack2 = []
        while(len(self.stack1) != 0):
            self.stack2.append(self.stack1.pop(0))
        removed = self.stack2.pop(0)
        while(len(self.stack2)!= 0):
            self.stack1.append(self.stack2.pop(0))
        return removed
            

class Test(unittest.TestCase):
    def testmyqueue(self):
        queue = MyQueue()
        queue.add(11)
        queue.add(22)
        queue.add(33)
        self.assertEqual(queue.remove(), 11)
        queue.add(44)
        queue.add(55)
        queue.add(66)
        self.assertEqual(queue.remove(), 22)
        self.assertEqual(queue.remove(), 33)
        self.assertEqual(queue.remove(), 44)
        self.assertEqual(queue.remove(), 55)
        queue.add(77)
        self.assertEqual(queue.remove(), 66)
        self.assertEqual(queue.remove(), 77)
        self.assertEqual(queue.remove(), None)


if __name__ == "__main__":
    unittest.main()