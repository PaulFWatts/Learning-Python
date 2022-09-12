frequency = [0,0,0,0,0,0,0,0,0,0]

number = int(input("Enter a number between 1 and 10: "))

while number != 0:
    frequency[number-1] += 1
    number = int(input("Enter a number between 1 and 10: "))
    

print()
print("Determing the frequency of numbers entered:")

count = 1
for item in frequency:
    if item != 0:
        print("Number:, %2d, frequency: %2d" % (count, item))
    count += 1

    