"""
Title: Creating a instance variables
Author: Jimmy
Date: March 2020
Purpose: To provide an example of instance variables in Python
"""

class ExampleClass:
    def doAdd(self, value1=0, value2=0):
        # mySum = value1 + value2
        self.mySum = value1 + value2
        # print ("The sum of %d plus %d is %d" %(value1, value2, mySum))
        print ("The sum of %d plus %d is %d" %(value1, value2, self.mySum))

    def printMySum(self):
        # print("The value of self.mySum is", mySum)
        print("The value of self.mySum is", self.mySum)

"""testing

from inst_p35 import ExampleClass
myThing = ExampleClass()
myThing.doAdd()
myThing.printMySum()
myThing.doAdd(2,3)
myThing.printMySum()

"""

