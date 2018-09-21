# -*- coding: utf-8 -*-
import unittest

class AnimalShelter():
    def __init__(self):
        self.current = 0
        self.doggo = []
        self.catto = []
    
    def enqueue(self, pet):
        if pet.__class__ == Dog: 
            self.doggo.append((pet, self.current))
            self.current += 1
        else:
            self.catto.append((pet, self.current))
            self.current += 1
    
    def dequeueDog(self):
        if (len(self.doggo) == 0):
            return None
        else:
            return self.doggo.pop(0)[0]
    def dequeueCat(self):
        if (len(self.catto) == 0):
            return None
        else:
            return self.catto.pop(0)[0]
    
    def dequeueAny(self):
        if (len(self.doggo) == 0):
            if (len(self.catto) == 0):
                return None
            else:
                return self.catto.pop(0)[0]
        elif (len(self.catto) == 0):
            print("entered")
            return self.doggo.pop(0)[0]
        else:
            if (self.doggo[0][1] > self.catto[0][1]):
                return self.catto.pop(0)[0]
            else:
                return self.doggo.pop(0)[0]

        

class Animal():
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name


class Dog(Animal): pass
class Cat(Animal): pass
        

class Test(unittest.TestCase):
    def testanimalshelter(self):
        shelter = AnimalShelter()
        shelter.enqueue(Dog("Hanzack"))
        shelter.enqueue(Dog("Pluto"))
        shelter.enqueue(Cat("Garfield"))
        shelter.enqueue(Cat("Tony"))
        shelter.enqueue(Dog("Clifford"))
        shelter.enqueue(Dog("Blue"))
        self.assertEqual(str(shelter.dequeueAny()), "Hanzack")
        self.assertEqual(str(shelter.dequeueAny()), "Pluto")
        self.assertEqual(str(shelter.dequeueDog()), "Clifford")
        self.assertEqual(str(shelter.dequeueDog()), "Blue")
        self.assertEqual(str(shelter.dequeueCat()), "Garfield")
        self.assertEqual(str(shelter.dequeueCat()), "Tony")
        self.assertEqual(str(shelter.dequeueAny()), "None")
        self.assertEqual(str(shelter.dequeueAny()), "None")







if __name__ == "__main__":
    unittest.main()
    
