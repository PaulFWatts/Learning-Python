'''This program demonstrates reading data
a line at a time from a file using a for loop
'''

f = open("myfile.txt",'r')

count = 1

for line in f:

   print(count,": ",line, end='')
   count += 1

f.close()
