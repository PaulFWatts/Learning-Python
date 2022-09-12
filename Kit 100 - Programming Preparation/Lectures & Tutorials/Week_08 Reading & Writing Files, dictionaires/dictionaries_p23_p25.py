'''python dictionaries '''

myDict = {'apples':1, 'oranges':5, 'bananas':12}
type(myDict) # a specific type - 'dict'
print(myDict)

print(myDict['apples'])
print(myDict['bananas'])

# print(myDict['pears']) # error

# Adding items:
myDict['pears'] = "who eats pears?"
print(myDict)

#get a list of keys
print(myDict.keys())
#get a list of values
print(myDict.values())

# iterate with each key to lookup a value
for aKey in myDict.keys():
   print(myDict[aKey])
