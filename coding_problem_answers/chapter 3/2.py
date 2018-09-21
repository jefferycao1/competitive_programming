# -*- coding: utf-8 -*-

import unittest


class stackmin:
    def __init__(self):
        self.top = None
        self._min = None
    
    def pop(self):
        if self.top is None:
            return None
        self._min = self._min.next
        item = self.top.data
        self.top = self.top.next
        return item
    
    
    def push(self, i):
        if (self._min is not None and i > self._min.data):
            self._min = Node(self._min.data, self._min)
        else:
            self._min = Node(i, self._min)
        self.top = Node(i, self.top)
    
    def min(self):
        if self._min is None:
            return None
        else:
            return self._min.data
    




class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        returnstring = str(self.data)
        
        if self.next:
            returnstring += " " + str(self.next)
        
        return returnstring




class Test(unittest.TestCase):
    def test_findmin(self):
            min_stack = stackmin()
            print("entered")
            self.assertEqual(min_stack.min(), None)
            min_stack.push(7)
            self.assertEqual(min_stack.min(), 7)
            min_stack.push(6)
            min_stack.push(5)
            self.assertEqual(min_stack.min(), 5)
            min_stack.push(10)
            self.assertEqual(min_stack.min(), 5)
            self.assertEqual(min_stack.pop(), 10)
            self.assertEqual(min_stack.pop(), 5)
            self.assertEqual(min_stack.min(), 6)
            self.assertEqual(min_stack.pop(), 6)
            self.assertEqual(min_stack.pop(), 7)
            self.assertEqual(min_stack.min(), None)


if __name__ == "__main__":
    unittest.main()