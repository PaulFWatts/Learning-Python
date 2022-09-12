'''Dictionaries  - A shopping cart example:
'''

item = input("Enter your cart item, 'quit' to exit: ")
cart = {}
while item != "quit":
   count = int(input("How many of this item? "))
   cart[item] = count
   item = input("Enter your cart item, 'quit' to exit: ")

print("You ordered the following things:")
for anItem in cart.keys(): 
   print("Item: %-10s"%anItem, "number: %-4d"%cart[anItem])
   
