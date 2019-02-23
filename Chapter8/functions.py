def greetings(username):
	"""Displays a simple greting."""
	print("Hello, " + username.title() + "!")

greetings("Victor")

def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet(pet_name='harry', animal_type='hamster')


def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# Jimi Hendrix

def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# Jimi Hendrix
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
# John Lee Hooker

def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
# Hello, Hannah!
# Hello, Ty!
# Hello, Margot!

greet_users('CUCU')
# Hello, C!
# Hello, U!
# Hello, C!
# Hello, U!

def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	for topping in toppings:
		print(" - " + topping)

make_pizza('pepperoni')
#  - pepperoni
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# - mushrooms
# - green peppers
# - extra cheese

def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) +
	"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein',
	location='princeton',
	field='physics')
print(user_profile)
