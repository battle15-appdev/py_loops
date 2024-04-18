""" Making Numerical Lists """

# Using the range() Function
for value in range (1,5):
	print(value)
	
'''	
This will only print 1 through 4. It only print the first value and 
stop at the second value.
An argument can be passed to the range() function, and the count will
start at 0. 

Ex range(6) >>> 0 - 5
'''

""" Using range() to make a List of Numbers """

# Wrap list() around a range() call to make a list of the numbers

numbers = list(range(1,6))
print(numbers)

''' 
Range can also be used to skip numbers within a range by adding 
a third argument 
'''

# Print all even numbers between 2 and 11
even_numbers = list(range(2,11,2))
print(even_numbers)

""" Make a list of the first 10 sqaured numbers """

# Create an empty list to add the squared numers to add they populate
squares = []

# for each number(value) in the range of 1 through 11
for value in range(1, 11):
	# Define square as the squared value of each number in the range
	square = value ** 2
	# Add the new value (square) to the empty list (squares) as it populates
	squares.append(square)
# print the newly created list of squared numbers
print(squares)

# A MORE CONSISE WAY

squares = []

for value in range (1,11):
	squares.append(value ** 2)
print(squares)


""" Simple Statistics with a List of Numbers """

# print minimun, maximum, sum of list of numbers:
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

""" List Comprehensions """

'''
List comprehensions allow you to generate a list using one line of code
combines the for loop and the creation of new elements into one line, 
and automatically appends each new element define the expression before
the for the values in the list of the loop.
No colon is used
'''

squares = [value**2 for value in range(1,11)]
print(squares)