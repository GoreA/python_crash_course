players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# ['charles', 'martina', 'michael']
print(players[1:4])
# ['martina', 'michael', 'florence']
print(players[:4])
# ['charles', 'martina', 'michael', 'florence']
print(players[2:])
# ['michael', 'florence', 'eli']
print(players[-3:])
# displays the last 3 elements
# ['michael', 'florence', 'eli']

for player in players[0:3]:
	print(player.title())
# Charles
# Martina
# Michael

my_food = ['pizza', 'falafel', 'carrot cake']

friend_food = my_food[:]
my_food.pop(1)
print(friend_food)
# ['pizza', 'falafel', 'carrot cake']

friend_food = my_food
print(friend_food)
# ['pizza', 'carrot cake']