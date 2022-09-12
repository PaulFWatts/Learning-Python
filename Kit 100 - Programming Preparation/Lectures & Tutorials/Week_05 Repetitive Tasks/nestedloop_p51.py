

print ("          Multiplication Table")
print ()
print ("-----------------------------------------------------")

for x in range(1, 10):
    print ("%3d" % x, "|", end="")
    
    for y in range (1,10):
        print ("%3d" % (x*y), end="")
    
    print ()
