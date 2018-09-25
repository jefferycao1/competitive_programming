# -*- coding: utf-8 -*-

class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter(self):
        return self.root.__iter__()
    
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = Node(key, val)
        
        self.size += 1
    
    def _put(self, key, val, currentNode):
        if (key < currentNode.key):
            if currentNode.hasleftchild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = Node(key, val, parent = currentNode)
        else:
            if currentNode.hasrightchild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = Node(key, val, parent = currentNode)
                
    def __setitem__(self, k, v):
        self.put(k, v)
        
        
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.data
            else:
                return None
        else:
            return None
        
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        elif key > currentNode.key:
            return self._get(key, currentNode.rightChild)
        
    def __getitem__(self, key):
        return self.get(key)


class Node:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    
    def hasleftchild(self):
        return self.leftChild
    
    def hasrightchild(self):
        return self.rightChild
    
    def isleftchild(self):
        return self.parent and self.parent.leftChild == self
    
    def isrightchild(self):
        return self.parent and self.parent.rightChild == self
    
    def isroot(self):
        return not self.parent
    
    def isleaf(self):
        return not (self.leftChild or self.rightChild)
    
    def hasanychildren(self):
        return self.rightChild or self.leftChild
    
    def hasbothchildren(self):
        return self.leftChild and self.rightChild
    
    def replacenodedata(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.leftChild = lc
        self.rightChild = rc
        if (self.hasleftchild()):
            self.leftChild.parent = self
        if (self.hasrightchild()):
            self.rightChild.parent = self
    
    
    
    
    
    