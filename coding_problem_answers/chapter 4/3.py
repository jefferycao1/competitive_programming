# -*- coding: utf-8 -*-

import unittest


def listdepth(tree):
    if tree is None:
        return []
    current_depth = -1
    lists = []
    node = tree
    queue = Queue()
    currenttail = None
    node.depth = 0
    while node:
        if (node.depth == current_depth):
            currenttail.next = ListNode(node.data)
            currenttail = currenttail.next
        else:
            current_depth = node.depth
            currenttail = ListNode(node.data)
            lists.append(currenttail)
        for child in [node.left, node.right]:
            if child is not None:
                child.depth = node.depth + 1
                queue.add(child)
        node = queue.remove()
    
    return lists




class TreeNode():
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.depth = None
    

class ListNode():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return str(self.data) + ',' + str(self.next)
    
class Queue():
    def __init__(self):
        self.queue = []
    
    def add(self, data):
        self.queue.append(data)
    
    def remove(self):
        if len(self.queue) == 0:
            return None
        else:
            item = self.queue[0]
            del self.queue[0]
            return item



class Test(unittest.TestCase):
  def test_list_of_depths(self):
    node_h = TreeNode('H')
    node_g = TreeNode('G')
    node_f = TreeNode('F')
    node_e = TreeNode('E', node_g)
    node_d = TreeNode('D', node_h)
    node_c = TreeNode('C', None, node_f)
    node_b = TreeNode('B', node_d, node_e)
    node_a = TreeNode('A', node_b, node_c)
    lists = listdepth(node_a)
    self.assertEqual(str(lists[0]), "A,None")
    self.assertEqual(str(lists[1]), "B,C,None")
    self.assertEqual(str(lists[2]), "D,E,F,None")
    self.assertEqual(str(lists[3]), "H,G,None")
    self.assertEqual(len(lists), 4)

if __name__ == "__main__":
    unittest.main()
    
