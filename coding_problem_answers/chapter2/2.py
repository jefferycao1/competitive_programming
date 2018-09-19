# -*- coding: utf-8 -*-
import unittest

def kthlast(head, k):
    answer, scout = head, head
    for _ in range(k):
        if scout is None:
            return None
        scout = scout.next
    while scout:
        answer = answer.next
        scout = scout.next
    return answer


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class Test(unittest.TestCase):
    def testkthlast(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, None)))))))
        self.assertEqual(None, kthlast(None, 0))
        self.assertEqual(1, kthlast(head, 7).data)
        self.assertEqual(4, kthlast(head, 4).data)

if __name__ == "__main__":
    unittest.main()
