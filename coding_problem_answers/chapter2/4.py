# -*- coding: utf-8 -*-

import unittest

def partition(head, pivot):
    node = head
    firsthead, firsttail = None, None
    secondhead, secondtail = None, None
    
    while node:
        if node.data < pivot:
            if firsthead is None:
                firsthead = node
                firsttail = firsthead
                
            else:
                firsttail.next = node
                firsttail = node
        else:
            if secondhead is None:
                secondhead = node
                secondtail = secondhead
            else:
                secondtail.next = node
                secondtail = node
        node = node.next
    
    if (firsthead is None):
        return secondhead
    else:
        firsttail.next = secondhead
        return firsthead
    



class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    def __str__(self):
        string = str(self.data)
        if(self.next):
            string += ',' + str(self.next)
        return string

class Test(unittest.TestCase):
    def testpartition(self):
        head1 = Node(7, Node(2, Node(9, Node(1, Node(6, Node(3, Node(8, None)))))))
        head2 = partition(head1, 6)
        self.assertEqual(str(head2), "2,1,3,7,9,6,8")



if __name__ == "__main__":
    unittest.main()