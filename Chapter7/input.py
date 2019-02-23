message = input("Tell me something, and I will repeat it back to you: ")
print(message)

age = '21'
if int(age) > 18:
	print("You can drink in Europe")

for num in range(1,31):
	if (num % 3 == 0):
		print(num**3)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")


