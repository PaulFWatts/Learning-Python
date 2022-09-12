'''This program demonstrates seeking to a position in a file'''

# example 1

f = open('myfile.txt','r')

line = f.readline()
print(line,end='')

f.seek(0) # 0 - resit to the first line

line = f.readline()
print(line,end='')

f.close()


# example 2
print()

f = open('myfile.txt','r')

line = f.readline()
print(line,end='')

f.seek(128) # resit depending on the table

line = f.readline()
print(line,end='')

f.close()
