current_number = 1;
while current_number < 31:
	if current_number % 3 == 0:
		print(current_number**3)
	current_number +=1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
# Verifying user: Candace
# Verifying user: Brian
# Verifying user: Alice

print(confirmed_users)
# ['candace', 'brian', 'alice']

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)







