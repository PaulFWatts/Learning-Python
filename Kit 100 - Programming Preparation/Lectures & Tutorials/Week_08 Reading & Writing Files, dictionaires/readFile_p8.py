'''This program demonstrates reading all data
from a file '''

f = open("myfile.txt", 'r')

allLines = f.read()

f.close()

print("Here is the data from the file:")

print(allLines)

