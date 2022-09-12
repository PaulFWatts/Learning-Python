"""
Title: Creating a class definition
Author: Jimmy
Date: March 2020
Purpose: To provide an example of class definition in Python
"""

class ExampleClass:
    greeting = ""

    def __init__(self, name = "there"):
        self.greeting = name + "!"

    def sayHello(self):
        print("Hello %s"%(self.greeting))


# test for output at shell
''' from exampleClass_p32 import ExampleClass
    myInstance = ExampleClass()
    myInstance.sayHello()
    myInstance = ExampleClass("Jimmy")
    myInstance.sayHello() '''
