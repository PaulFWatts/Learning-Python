rate= float(input("Enter the exchange rate from dollars to RMB: "))
conversionType = int(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

if conversionType == 0:
    dollars =  float(input("Enter the dollar amount: "))
    RMB = dollars * rate
    print(format(dollars, ".2f"), "dollars is", format(RMB, ".2f"), "Yuan")
elif conversionType == 1:
    RMB = float(input("Enter the RMB amount: "))
    dollars = RMB / rate
    print(format(RMB, ".2f"), "Yuan is", format(dollars, ".2f"), "dollars")
else:
    print("Incorrect input")

print("Program ends.")
