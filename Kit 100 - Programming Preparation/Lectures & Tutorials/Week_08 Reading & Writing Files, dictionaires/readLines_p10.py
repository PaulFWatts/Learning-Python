'''This program demonstrates reading data
a line at a time from a file
'''

# example 1

f = open("myfile.txt",'r')

print("here is the data from the file, a line at a time:")
print()

# note: each call to readline() will return a different (the next) line from the file.
line = f.readline()
print(line)

line = f.readline()
print(line)

line = f.readline()
print(line)

line = f.readline()
print(line)

line = f.readline()
print(line)

line = f.readline()
print(line)

f.close()


# example 2 - avoid to return a new line

f = open("myfile.txt",'r')

print("here is the data from the file, a line at a time:")
print()

line = f.readline()
print(line, end='') # add end='' to aviod to return a new line

line = f.readline()
print(line, end='')

line = f.readline()
print(line,end='')

line = f.readline()
print(line,end='')

line = f.readline()
print(line,end='')

line = f.readline()
print(line,end='')

line = f.readline() #return an empty when no more lines to read 
print(line,end='')

f.close()

