def get_name():
   # get the user's first and last name
   first = input("Enter your first name: ")
   last = input("Enter your last name / surname: ")
   # return both names
   return first,last

first,last = get_name()
print(first + " " + last)
