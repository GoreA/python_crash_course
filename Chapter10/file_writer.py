programming = 'programming.txt'

with open(programming, 'w') as file_object:
	file_object.write("I love programming.\n")

with open(programming) as file_object:
	file = file_object.read()

print(file)

