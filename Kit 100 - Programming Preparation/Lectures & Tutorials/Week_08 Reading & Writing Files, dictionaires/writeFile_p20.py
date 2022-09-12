'''This program demonstrates writing data
a line at a time to a file '''

f = open('aNewFile.txt','a')

age = 30
name = "Zehong Jimmy Cao"
f.write("Age:" + str(age) + "\n")
f.write("Name:" + name + "\n")


f.close()
