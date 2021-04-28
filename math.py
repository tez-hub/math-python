# import math for log

import math

print("Welcome to the simple math helper.")
print("What would you like to calculate?.")

# Display choices for the user
print("1. Sqrt")
print("2. Log")
print("3. Factorial")

# Allow user to input a choice
choice = int(input("> "))

# Conditions
if choice < 0:
   print("Enter a valid choice.")
elif choice == 0:
   print("Choice must be greater than 0")
elif choice == 1:
   print("Enter the number to get the Sqrt: ")

   # have int after print to make the answer an integer and not double
   print(int(math.sqrt(int(input("> ")))))
elif choice == 2:
   print("Enter the number to get the logarithm: ")
   
   # have int after print to make the answer an integer and not double
   print(int(math.log10(int(input("> ")))))

elif choice == 3:
   print("Enter the number to factorial: ")
   num = int(input("> "))

   factorial = 1

   # Reject numbers less than 0
   if num < 0:
      print("Sorry, factorial does not exist for negative numbers")
   elif num == 0:
      print("1")
   else:
      for i in range(1,num + 1):
         factorial = factorial*i
      print(factorial)
