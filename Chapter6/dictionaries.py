alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# green
# 5

del alien_0['points']

alien_0['x_pos'] = 50
alien_0['y_pos'] = 0
print(alien_0)
# {'color': 'green', 'points': 5, 'x_pos': 50, 'y_pos': 0}

alien_0['color'] = 'yellow'
print(alien_0['color'])

alien_0 = {'x_pos' : 0, 'y_pos' : 0, 'speed' : 'medium'}
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print("New x-position: " + str(alien_0['x_pos']))

person = {
	'first_name' : 'Victor',
	'last_name' : 'Grigore',
	'age' : '29',
	'city' : 'Ulan-Bator',
}

for key, val in person.items():
	print("\nKey: " + key)
	print("Value: " + val)

for key in sorted(person.keys()):
	print("Key: " + key)
# Key: age
# Key: city
# Key: first_name
# Key: last_name

for val in person.values():
	print("Value: " + val)
# Value: Victor
# Value: Grigore
# Value: 29
# Value: Ulan-Bator

names = ['first_name', 'last_name']
for name in names:
	if name in person.keys():
		print (name + " : " + person[name].title())
# first_name : Victor
# last_name : Grigore

favorite_numebers = {}
persons = ['Alina', 'Maria', 'Diana', 'Doina', 'Alina', 'Veronica']

for person in persons:
	favorite_numebers[person] = 1

for num in set(favorite_numebers.values()):
	print(num)







