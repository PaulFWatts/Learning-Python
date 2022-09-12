'''This program demonstrates writing data
a line at a time to a file'''

age = 2021
name = "Bill J"

f = open('aNewFile.txt','a')

f.write("Age:" + str(age)+ "\n")
f.write("Name:" + name)

f.close()
