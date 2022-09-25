"""
If you have two dictionaries that you want to combine, you can
combine them using two easy methods. You can use the merge
( I ) operator or the ( ** ) operator. Below, we have two
dictionaries, a and b. We are going to use these two methods to
combine the dictionaries.
"""
# Method 1
print("Method 1")
name1 = {"kelly": 23, "Derick": 14, "John": 7}
name2 = {"Ravi": 45, "Mpho": 67}
print("name1: ", name1)
print("name2: ", name2)
names = name1 | name2
print("names: ", names)
# Method 2
print("Method 2")
name3 = {"kelly": 23, "Derick": 14, "John": 7}
name4 = {"Ravi": 45, "Mpho": 67}
print("name3: ", name3)
print("name4: ", name4)
names = {**name3, **name4}
print("names: ", names)
# Method 3
print("Method 3")
name5 = {"kelly": 23, "Derick": 14, "John": 7}
name6 = {"Ravi": 45, "Mpho": 67}
print("name5: ", name5)
print("name6: ", name6)
names = dict(name5, **name6)
print("names: ", names)
# Method 4
print("Method 4")
name7 = {"kelly": 23, "Derick": 14, "John": 7}
name8 = {"Ravi": 45, "Mpho": 67}
print("name7: ", name7)
print("name8: ", name8)
names = dict(**name7, **name8)
print("names: ", names)
