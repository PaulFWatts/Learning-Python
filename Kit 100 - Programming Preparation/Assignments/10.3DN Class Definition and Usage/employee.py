'''
10.3DN Class Definition and Usage - Employee Class
Author: Paul Watts 569987
Date: May, 2022

This program defines a class called Employee with the following attributes:
    * name (Employee name)
    * idNumber (Employee ID number)
    * department (Employee department)
    * jobTitle (Employee job title)
    
'''

class Employee:
    
    def __init__(self, name, idNumber, department, jobTitle): # Constructor
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.jobTitle = jobTitle
        
    # Define "getters" for the attributes
    
    def getName(self):
        return self.name
    
    def getEmployeeID(self):
        return self.idNumber
    
    def getDepartment(self):
        return self.department
    
    def getTitle(self):
        return self.jobTitle
    
    # Define "setters" for the attributes
    
    def setName(self, name):
        self.name = name
        
    def setEmployeeID(self, idNumber):
        self.idNumber = idNumber
        
    def setDepartment(self, department):
        self.department = department
        
    def setTitle(self, jobTitle):
        self.jobTitle = jobTitle
        
    # Define a "toString" method
    def __str__(self):
        return self.name + "Id Number: " + self.idNumber + "Department: " + self.department + "Job Title: " + self.jobTitle
        
    
        
    
    


