# -*- coding: utf-8 -*-
import linkedlist
import unittest


def removedups(head):
    node = head
    if node:
        values = {node.data: True}
        while node.next:
            if (node.next.data in values):
                node.next = node.next.next
            else:
                values[node.next.data] = True
                node = node.next
    return head





class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Test(unittest.TestCase):
    def testdups(self):
        head = Node(1, Node(3, Node(4, Node(1, Node(5, None)))))
        removedups(head)
        self.assertEqual(head.data, 1)
        self.assertEqual(head.next.data, 3)
        self.assertEqual(head.next.next.data, 4)
        self.assertEqual(head.next.next.next.data, 5)
        self.assertEqual(head.next.next.next.next, None)


if __name__ == "__main__":
    lst = linkedlist.LinkedList()
    unittest.main()
    