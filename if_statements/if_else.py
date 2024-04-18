""" 
Similar to an if statement, but the else statement is excuted 
if the conditional test fails 
"""
# Check If the person can vote based on age
age = 17
#age = 19 
if age >= 18:
	print(" You are old enough to vote!")
	# This next line will run in this loop as long as the condtions are meet
	print(" Have you registered to vote yet?")

else:
	print("Sorry, you are too young to vote.")
	print("Please register as soon are you turn 18")