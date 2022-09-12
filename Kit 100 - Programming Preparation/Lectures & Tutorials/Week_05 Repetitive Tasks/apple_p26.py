'''
Title: for loop Example

Purpose: To demonstrate how a for loop works with
         the string 'apple'
'''

letterNum = 1

for letter in "Apple":

  # print ("Letter", letterNum, "is", letter)
  # alternatively - use operator control print %
  print ("Letter %d is %s" % (letterNum,  letter)) 

  letterNum += 1

