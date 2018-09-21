# -*- coding: utf-8 -*-
import unittest


class SetOfStacks:
    def __init__(self, maxplates):
        self.maxplates = maxplates
        self.head = []
    
    def pop(self):
        while (len(self.head) and len(self.head[-1]) == 0):
            self.head.pop()
        if (len(self.head) == 0):
            return None
        item = self.head[-1].pop()
        if (len(self.head[-1]) == 0):
            self.head.pop()
        return item
    
    def push(self, i):
        if len(self.head) and (len(self.head[-1]) < self.maxplates):
            self.head[-1].append(i)
        else:
            self.head.append([i])
    
    def pop_at(self, i):
        if (len(self.head[i]) == 0):
            return None
        elif (len(self.head[i]) == 1):
            item = self.head[i].pop()
            return item
        else:
            item = self.head[i].pop()
            return item

class Test(unittest.TestCase):
    def test_setofstacks(self):
            stack = SetOfStacks(3)
            stack.push(11)
            stack.push(22)
            stack.push(33)
            stack.push(44)
            stack.push(55)
            stack.push(66)
            stack.push(77)
            stack.push(88)
            self.assertEqual(stack.pop(), 88)
            self.assertEqual(stack.pop_at(1), 66)
            self.assertEqual(stack.pop_at(0), 33)
            self.assertEqual(stack.pop_at(1), 55)
            self.assertEqual(stack.pop_at(1), 44)
            self.assertEqual(stack.pop_at(1), None)
            stack.push(99)
            self.assertEqual(stack.pop(), 99)
            self.assertEqual(stack.pop(), 77)
            self.assertEqual(stack.pop(), 22)
            self.assertEqual(stack.pop(), 11)
            self.assertEqual(stack.pop(), None)





if __name__ == "__main__":
    unittest.main()