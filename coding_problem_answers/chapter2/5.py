# -*- coding: utf-8 -*-

import unittest

def sumlists(list1, list2):
    carry = 0
    resulthead, resultnode = None, None
    
    while list1 or list2 or carry:
        nextnum = carry
        if list1:
            nextnum += list1.data
            list1 = list1.next
        if list2:
            nextnum += list2.data
            list2 = list2.next
        if resultnode:
            resultnode.next = Node(nextnum % 10, None)
            resultnode = resultnode.next
        else:
            resultnode = Node(nextnum % 10, None)
            resulthead = resultnode
        
        carry = int(nextnum / 10)
    return resulthead

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __str__(self):
        string = str(self.data)
        if self.next:
            string += "," + str(self.next)
        return string

class Test(unittest.TestCase):
    def testsumlists(self):
        num1 = Node(7, Node(1, Node(6, None)))
        num2 = Node(5, Node(9, Node(2, None)))
        ans = sumlists(num1, num2)
        self.assertEqual(str(ans), "2,1,9")
        
        

if __name__ == "__main__":
    unittest.main()