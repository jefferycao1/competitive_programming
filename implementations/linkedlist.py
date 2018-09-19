# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, newnext):
        self.next = newnext
        
    def __str__(self):
        return str(self.data)
#singly linked linkedlist implementation


class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insert(self, data):
        newnode = Node(data, self.head)
        self.head = newnode
        
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.data == data:
                found = True
            else:
                current = current.next
        if current is None:
            raise ValueError("Data is not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError("Data is not in list")
        if previous is None:
            self.head = current.next
        else:
            previous.set_next(current.next)

    def __str__(self):
        current = self.head
        string = ""
        while(current):
            string += str(current.get_data()) + " -> "
            current = current.next
        string += "NULL"
        return string








