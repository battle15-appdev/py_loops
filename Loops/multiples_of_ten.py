"""
This program uses while loops to detemine whether a number 
that a user input is a multiple of ten
"""

number = input("Please enter a number and I will tell you if it is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print (f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")