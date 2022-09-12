'''This program demonstrates reading data
a line at a time from a file using a while loop
'''

f = open("myfile.txt",'r')

line = f.readline()
count = 1

while line != '':
   print(count,": ",line,end='')
   # print(count,": ",line)
   line = f.readline()
   count += 1
   
f.close()
