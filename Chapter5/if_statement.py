cars = ['audi', 'ford', 'bmw', 'mergedes-bens']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
# Audi
# Ford
# BMW
# Mergedes-Bens

age_0 = 22
age_1 = 18
print(age_0 > 18 and age_1 != 42)
# True

print(age_0 == 22 or age_1 == 42)
# True

print('toyota' in cars)
# False

print('skoda' not in cars)
# True

age = 12
if (age < 4):
	print("Your admission cost is $0.")
elif (age <19):
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
# Your admission cost is $5.

requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + "!")
	else:
		print("Sotty, we don't have " + requested_topping + "!")
# Adding mushrooms!
# Sotty, we don't have french fries!
# Adding extra cheese!









