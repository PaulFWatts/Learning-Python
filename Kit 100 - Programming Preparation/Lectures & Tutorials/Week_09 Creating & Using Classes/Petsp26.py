"""
Title: Creating a class definition pt 2
Author: Zehong Jimmy Cao
Date: March 2020
Purpose: To provide an example of class definition in Python
"""

class Pet:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return ("%s is a %s") % (self.name, self.species)
    


  
