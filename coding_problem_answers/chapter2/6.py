# -*- coding: utf-8 -*-
import unittest

def reverse(head):
    reverse = None
    node = head
    while node:
        newnode = Node(node.data, None)
        newnode.next = reverse
        reverse = newnode
        node = node.next
    return reverse
    
def palindrome(head):
    reverselist = reverse(head)

    while head and reverselist:
        if head.data != reverselist.data:
            return False
        head = head.next
        reverselist = reverselist.next
    
    return head is None and reverselist is None



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
        num1 = Node(7, Node(1, Node(1, Node(7, None))))
        #num2 = Node(5, Node(9, Node(2, None)))
        ans = palindrome(num1)
        self.assertEqual(ans, True)
        
        

if __name__ == "__main__":
    unittest.main()