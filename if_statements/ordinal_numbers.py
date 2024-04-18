"""
Ordinal numbers have different endings
Ex. 1st, 2nd, 3rd, 4th
This program will print a list of ordinal numbers from 1 to 9
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through the list
for number in numbers:

	if number == 1:
		print (f"{number}st")
	elif number == 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")