my_foods = ['pizza','falafel','carrot cake']

friends_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("My friend's foods favorite foods are:")
print(friends_foods)

my_foods.append('canoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

# Write two for loops to print each list of foods
# 1

print("My foods")
for food in my_foods[:]:
	print(food)

# 2

print("\nFriend's foods")
for food in friends_foods[:]:

	print(food)