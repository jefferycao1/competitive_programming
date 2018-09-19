# -*- coding: utf-8 -*-

import unittest

def deletemiddle(node):
    placeholder = node.next
    node.data = placeholder.data
    node.next = placeholder.next


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    

class Test(unittest.TestCase):
    def testdeletemiddle(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
        deletemiddle(head.next.next)
        self.assertEqual(head.data, 1)
        self.assertEqual(head.next.data, 2)
        self.assertEqual(head.next.next.data, 4)
        self.assertEqual(head.next.next.next.data, 5)

if __name__ == "__main__":
    unittest.main()