# -*- coding: utf-8 -*-
import unittest

def minheight(array):
    if (len(array) == 0):
        return None
    
    middle = int(len(array) / 2)
    left = minheight(array[:middle])
    right = minheight(array[(middle + 1):])
    return BST(array[middle], left, right)




class BST():
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        
        returnstring = ""
        if self.left: returnstring += str(self.left)
        returnstring += str(self.data)
        if self.right: returnstring += str(self.right)

        return returnstring



class Test(unittest.TestCase):
    def testbst(self):
        sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        bst = minheight(sorted_array)
        self.assertEqual(str(bst), "(5(3(2(1..).)(4..))(8(7(6..).)(9..)))")

if __name__ == "__main__":
    unittest.main()

        
