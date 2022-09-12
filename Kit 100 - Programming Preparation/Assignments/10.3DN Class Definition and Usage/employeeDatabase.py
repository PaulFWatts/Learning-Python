'''
10.3DN Class Definition and Usage - Employee Database
Author: Paul Watts 569987
Date: May, 2022

This program imports the Employee class from the employee.py file.
It uses this class to create five Employee objects and prints them in the
required assignment format
    
'''

import employee

listOfEmployees = [] # Create a list for Employee objects

# Create five Employee objects and apend to our list
listOfEmployees.append(employee.Employee("Darth Vader", "123456", "Empire", "Supreme Leader"))
listOfEmployees.append(employee.Employee("Luke Skywalker", "246810", "Rebellion","Red 5 Leader"))
listOfEmployees.append(employee.Employee("Han Solo", "135790", "Acquistions", "Chief Smuggler"))
listOfEmployees.append(employee.Employee("Leia Organa", "888888", "Royalty", "Princess"))
listOfEmployees.append(employee.Employee("Chewbacca", "111112", "IT", "CTO"))

# Print Heading
print("\nName\t\t\tId Number\tDepartment\tJob Title")
print("----\t\t\t---------\t----------\t---------")

# Print the Employee objects
for employee in listOfEmployees:   
    print(f"{employee.getName()}\t\t{employee.getEmployeeID()}\t\t{employee.getDepartment():11s}\t{employee.getTitle()}")

