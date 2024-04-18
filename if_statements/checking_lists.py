""" Checking Whether a Value Is in a List"""

# Using the keyword IN

# Check for toppings
requested_toppings = ['mushrooms','onions','pineapple']
true_false = 'mushrooms' in requested_toppings
print(true_false)
# Retuns True

true_false = 'pepperoni' in requested_toppings
print(true_false)
# Returns False

""" Checking Where a Value Is Not in a List """
# Using the keyword NOT

# Checking if user has been banned
banned_users =['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish")

''' Python returns True when the line was executed '''

""" Boolean Expressions """

''' 
A Boolean value is either True or False and is
often used to keep track of certain conditions
'''
game_active = True
can_edit = False