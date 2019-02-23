alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

aliens = []
for alien_number in range(1, 31):
	aliens.append({'color' : 'green', 'points' : 5})

print("Total number of aliens: " + str(len(aliens)))
# Total number of aliens: 30

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

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
# Quattro Formaggi contains: 
# tomatoes
# extra cheese
# Quattro Stagioni contains: 
# tomatoes
# extra meat

users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	},
}
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
# Username: aeinstein
# 	Full name: Albert Einstein
# 	Location: Princeton

# Username: mcurie
# 	Full name: Marie Curie
# 	Location: Paris



