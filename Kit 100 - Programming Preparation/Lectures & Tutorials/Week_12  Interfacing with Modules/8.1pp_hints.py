#8.1PP for hints only.

def getChecksum(barcode):
   
   total = 0
   count = 0
  
   for letter in barcode:

      if letter.isdigit(): 
         
         total
         count 

   return total,count

def main():
   
   answer = 'y'
   
   while answer == 'y':
     
      barcode = input("Enter the barcode:")
      
      checksum,digitCount = getChecksum(barcode)
      
      print("The checksum and digits")
     
      answer = input("Do you want to run this again? (y/n):")

   print("goodbye!")

main()
