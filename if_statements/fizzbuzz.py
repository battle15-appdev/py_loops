
"""
1 - 100
Mulitple of 3: 'fizz'
Multiple of 5: 'buzz'
Multiple of 3 AND 5: 'fizz buzz'
"""

numbers = list(range(1,101))

# Loop though the list 'numbers'
for number in numbers:
	if number % 15 == 0:
		print('Fizzbuzz')
	elif number % 3 == 0:
		print('Fizz')
	elif number % 5 == 0:
		print('Buzz')
	else:
		print(number)
