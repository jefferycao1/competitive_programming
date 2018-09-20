# -*- coding: utf-8 -*-
import unittest



def intersection(head1, head2):
    nodes = {}
    currentnode = head1
    while(currentnode):
        nodes[currentnode] = 1
        currentnode = currentnode.next
    
    othernode = head2
    while(othernode):
        if othernode in nodes:
            return othernode
        othernode = othernode.next
    return None
    
    

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
    def testsumlists(self):
        head1 = Node(10,Node(20,Node(30)))
        head2 = Node(20,Node(30,Node(40)))
        self.assertEqual(intersection(head1, head2), None)
        node = Node(70,Node(80))
        head3 = Node(50,Node(20,node))
        head4 = Node(60,Node(90,Node(10,node)))
        self.assertEqual(intersection(head3, head4), node)
        
        

if __name__ == "__main__":
    unittest.main()