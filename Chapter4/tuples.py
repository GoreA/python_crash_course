dimensions = (200, 50)
# dimensions[0] = 150
# TypeError: 'tuple' object does not support item assignment

for dimension in dimensions:
	print(dimension)

dimensions = (150, 50)
for dimension in dimensions:
	print(dimension)