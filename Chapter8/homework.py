# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(title):
	print("One of my favorite books is \"" + title.title() + "\".")

favorite_book("Cehov. Raskazy")

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.
def make_shirt(size, message):
	print("You made a shirt with message \"" + message + "\" and it is " + size + " size." )

make_shirt("L", "Os Tincoas")

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
def make_shirt2(size = "L", message = "I love Python"):
	print("You made a shirt with message \"" + message + "\" and it is " + size + " size." )

make_shirt2()
make_shirt2("M")
make_shirt2("S", "Cucu!")

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.
def describe_city(city, country="Moldova"):
	print(city.title() + " is in " + country.title() + ".")

describe_city("Cahul")
describe_city("Kabul", "Afganistan")
describe_city(country = "Australia", city = "Melbourn")

# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.
def city_country(city, country):
	return city + ", " + country

print(city_country('Brasil', 'Brasil'))
print(city_country('Mexico', 'Mexico'))
print(city_country('Jakarta', 'Indonesia'))

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number
# of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.
def make_album(artist_name, album_title, number_of_tracks = 0):
	album = {
		'artist_name' : artist_name,
		'album_title' : album_title,
		}
	if number_of_tracks != 0:
		album['number_of_tracks'] = number_of_tracks
	return album

print(make_album("Os Tincoas", "Dadinho e Mateus"))
print(make_album("Alla Borisovna Pugaciova", "Da!", 14))

# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list.
magicians = ['Dante', 'Harry Blackstone Sr.', 'David Blaine', 'Harry Houdini', 'David Copperfield']

def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())

show_magicians(magicians)

# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.
def make_great(magicians):
	while magicians:
		magician = magicians.pop()
		print("Great " + magician)

make_great(magicians)
show_magicians(magicians)

# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original
# names and one list with the Great added to each magician’s name.
magicians = ['Dante', 'Harry Blackstone Sr.', 'David Blaine', 'Harry Houdini', 'David Copperfield']
make_great(magicians[:])
show_magicians(magicians)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that is being ordered. Call the function three times, using a different number
# of arguments each time.
def make_sandwich(*ingredients):
	for inredient in ingredients:
		print(" - " + inredient)

make_sandwich('bread', 'tomatoes', 'chees')

# 8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
# a profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

profile = build_profile('Al', 'Gore', job = 'Vice President', country = 'USA', year_of_birth = '1948')
print(profile)
# Actually those are my last and first names :P

# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.
def make_car(manufacturer, model, **details):
	car = {}
	car['manufacturer'] = manufacturer
	car['model'] = model
	for key, value in details.items():
		car[key] = str(value)
	return car

car = make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)





