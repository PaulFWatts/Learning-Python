'''
10.2CR Class Definition
Author: Paul Watts 569987
Date: May, 2022

This program defines a class called Animal, which has the following attributes:
    * name (a string, the animals adopted name)
    * animalType (a string, the sort of animal, for example, dog, cat, etc.)
    * age (an integer, the animals estimated age)
    * adopted (a boolean, whether the animal has been accepted for adoption yet)
    
'''

class Animal:

    def __init__(self, name, animalType, age, adopted): # Constructor    
        self.name = name
        self.animalType = animalType
        self.age = age
        self.adopted = adopted
    
    # Define "getters" for class Animal
    def  getName(self):
        return self.name
    
    def getAnimalType(self):
        return self.animalType
    
    def getAge(self):
        return self.age
    
    def getAdopted(self):
        return self.adopted
    
    #Define "setters" for class Animal
    def setName(self, name):  
        self.name = name
        
    def setAnimalType(self, animalType):
        self.animalType = animalType
        
    def setAge(self, age):
        self.age = age
        
    def setAdopted(self, adopted):
        self.adopted = adopted
                 
                
    # Define "toString" for class Animal
    def __str__(self):
        message = "Name: " + self.name + "Type: " + self.animalType + "Age: " + str(self.age) + "Adopted: " + str(self.adopted)
        return message
        
        
        
        
