# -*- coding: utf-8 -*-
import unittest

def loopdetection(head):
    node = head
    nodesvisited = {}
    while (node):
        if (node not in nodesvisited):
            nodesvisited[node] = 1
        else:
            return node
        node = node.next
    

class Node():
    def __init__(self, data, next= None):
        self.data = data
        self.next = next
    
    def __str__(self):
        string = str(self.data)
        if self.next:
            string += "," + str(self.next)
        return string

class Test(unittest.TestCase):
    def testloopdetection(self):
            head1 = Node(100,Node(200,Node(300)))
            self.assertEqual(loopdetection(head1), None)
            node1 = Node(600)
            node2 = Node(700,Node(800,Node(900,node1)))
            node1.next = node2
            head2 = Node(500,node1)
            self.assertEqual(loopdetection(head2), node1)
        

if __name__ == "__main__":
    unittest.main()