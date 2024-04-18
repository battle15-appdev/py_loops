# Rivers: Make a list containing three major rivers:

rivers = {
	'Nile':'Egypt',
	'Mississippi':'U.S.A',
	'Yangtze': "China"
}

# Use a loop to print a sentence about each river
# "The Nile runs through the Egypt"

for river, country in rivers.items():
	print(f"{river.title()} runs through {country.title()}")

# Use a loop to print the name of teach river included in the dictionary
for river in rivers.keys():
	print(f"River: {river}")

# Use Use a loop to print the name of each country included in the dictionary

for country in rivers.values():
	print(f"Country: {country}")
