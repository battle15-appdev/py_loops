"""Check usernames to make sure that desired username is available"""

# List of usernames that have already been created
current_users = ['tom1','admin','mary2','cindy1','lucy5']

# List of new users who want to create usernames
# Two of the usernames are in the current_users list to check against
new_users = ['steven4','tom1','aDmIn','BOB','Jack1e']


# running to compare new_user list against current_user list
for username in new_users:
	
    # Making sure the comparison is case insensitive
	if username.lower() in current_users:
		# If the username is availible
		print(f"Username, {username}, is taken")
	else: 
		#if the username has not been used
		print(f"Username, {username}, is Available")
