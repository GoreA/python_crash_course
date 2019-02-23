# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {
	'romania' : 'Dunarea',
	'moldova' : 'Nistru',
	'rusia' : 'Lena',
	'germany' : 'Dunarea',
	'egypt' : 'Nile',
}

for country in rivers:
	print("The " + rivers[country].title() + " runs through " + country.title() + ".")

for country in rivers.keys():
	print(country)

for river in set(rivers.values()):
	print(river)

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person

person_0 = {
	'first_name' : 'Victor',
	'last_name' : 'Grigore',
	'age' : '29',
	'city' : 'Ulan-Bator',
}

person_1 = {
	'first_name' : 'Maria',
	'last_name' : 'Toma',
	'age' : '23',
	'city' : 'Praha',
}

person_2 = {
	'first_name' : 'Irina',
	'last_name' : 'Cehova',
	'age' : '32',
	'city' : 'Moscva',
}

persons = [person_0, person_1, person_2]
details = ""
for person in persons:
	for value in person.values():
		details = details + value + " "
	print(details)
	details = ""
# Victor Grigore 29 Ulan-Bator 
# Maria Toma 23 Praga 
# Irina Cehova 32 Moscva 

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.
favorite_places = {
	'Maria' : ['Geneva', 'Praha', 'Milano'],
	'Victor' : ['Praha', 'Lvov', 'Odessa'],
	'Irina' : ['Moscva', 'Ulan-Bator', 'Singapore']
}

for name, places in favorite_places.items():
	print(name.title() + " likes ")
	for place in places:
		print("\t" + place.title()) 
# Maria likes 
# 	Geneva
# 	Praga
# 	Milano
# Victor likes 
# 	Praga
# 	Lvov
# 	Odessa
# Irina likes 
# 	Moscva
# 	Ulan-Bator
# 	Singapore

# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.
praha = {
	'name' : 'Praha',
	'country' : 'Česko',
	'population' : 1300000,
	'fact' : 'historical capital of Bohemia'
}

moskva = {
	'name' : 'Moskva',
	'country' : 'Rossia',
	'population' : 17000000,
	'fact' : 'the largest city (both by population and by area) entirely on the European continent'
}

ulan_bator = {
	'name' : 'Ulaanbaatar',
	'country' : 'Mongol Uls',
	'population' : 1300000,
	'fact' : 'founded in 1639 as a nomadic Buddhist monastic centre'
}

cities = [praha, moskva, ulan_bator]
for city in cities:
	for key, value in city.items():
		print(key + ": ")
		print("\t" + str(value))
	print("\n")

# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values, changing
# the context of the program or improving the formatting of the output.
pizza_0 = { 
	'name' : 'Quattro Formaggi',
	'crust': 'thick',
	'toppings': ['tomatoes', 'extra cheese'],
}

pizza_1 = { 
	'name' : 'Quattro Stagioni',
	'crust': 'thick',
	'toppings': ['tomatoes', 'extra meat'],
}

pizzas = [pizza_0, pizza_1]

for pizza in pizzas:
	print(pizza['name'].title() + " contains: ")
	for topping in pizza['toppings']:
		print(topping)