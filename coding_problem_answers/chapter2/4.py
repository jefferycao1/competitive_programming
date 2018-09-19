# -*- coding: utf-8 -*-

import unittest

def partition(head, pivot):
    node = head
    firsthalf = None
    secondhalf = None
    
    while node:
        if node.data < pivot:
            if firsthalf:
                firsthalf.next = node
            else:
                






class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    def __str__(self):
        string = str(self.data)
        if(self.next):
            string += ' -> ' + str(self.next)
        return string

class Test(unittest.TestCase):
    def testpartition(self):
        



if __name__ == "__main__":
    unittest.main()