# Demonstration of exception handling
valid = False


while (not(valid)):

   try:
       value = int(input("Type a number between 1 and 10: "))
   
   except ValueError:
       print("You must type a number between 1 and 10!")

   else:
       valid = True
       if (value > 0) and (value <= 10):
           print("You typed: %s" % value)
       else:
           print("The value you typed is incorrect!")
