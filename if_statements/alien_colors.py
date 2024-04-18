
"""if-elif-else chain"""

'''
Based on which alien color the user shoots down, 
print how much the user scored

Green: print message for earned 5 points
Yellow: print message for earned 10 points
Red: print messgae for earned 15 points
'''

# Green Alien

alien_color = 'green'

if alien_color == 'green':
	print("5 points scored")
elif alien_color == 'yellow':
	print("10 points scored")
else:
	print("15 points scored")

# Yellow Alien
alien_color = 'yellow'

if alien_color == 'green':
	print("5 points scored")
elif alien_color == 'yellow':
	print("10 points scored")
else:
	print("15 points scored")

# Red Alien

alien_color ='red'
	
if alien_color == 'green':
	points = 5
elif alien_color == 'yellow':
	points = 10
else:
	points = 15

print(f"{points} points scored")
