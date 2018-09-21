# -*- coding: utf-8 -*-

import unittest


class Threestack:
    def __init__(self):
        self.stack = [[], [], []]
    
    def push(self, i, arraynum):
        if (abs(arraynum) > 2):
            raise Exception("input either 0, 1, 2")
        else:
            self.stack[arraynum].append(i)
    
    def pop(self, arraynum):
        if(abs(arraynum) > 2):
            raise Exception("input either 0, 1, 2")
        else:
            return self.stack[arraynum].pop()
    
        
        

class Test(unittest.TestCase):
    def testthreestack(self):
        teststack = Threestack()
        teststack.push(141, 0)
        teststack.push(121, 1)
        teststack.push(131, 2)
        teststack.push(151, 0)
        self.assertEqual(teststack.pop(0), 151)
        self.assertEqual(teststack.pop(1), 121)
        self.assertEqual(teststack.pop(2), 131)
        



if __name__ == "__main__":
    unittest.main()
