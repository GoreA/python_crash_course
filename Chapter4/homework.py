# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
for value in range(1, 21):
	print(value)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)
for num in range(1, 1000001):
	print(value)

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
million = range(1, 1000001)
print(sum(million))
print(min(million))
print(max(million))
# Output:
# 500000500000
# 1
# 1000000
# [Finished in 2.4s]

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.
for odd_num in range(1, 20, 2):
	print(odd_num)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
multiples_of_three = list(num * 3 for num in range(1, 11))
print(multiples_of_three)

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
cubes = []
for num in range(1, 11):
	cubes.append(num**3)
for cube in cubes:
	print(cube)
# Output:
# 1
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729
# 1000

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
cubes = list(value ** 3 for value in range(1, 11))
print(cubes)
# Output:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# • Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.
my_food = ['pizza', 'falafel', 'carrot cake', 'cheescacke', 'ice cream']
print("The first three items in the list are:")
print(my_food[:3])
print("Three items from the middle of the list are:")
print(my_food[1:4])
print("The last three items in the list are:")
print(my_food[-3:])
# The first three items in the list are:
# ['pizza', 'falafel', 'carrot cake']
# Three items from the middle of the list are:
# ['falafel', 'carrot cake', 'cheescacke']
# The last three items in the list are:
# ['carrot cake', 'cheescacke', 'ice cream']


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.
my_pizza = ['Carbonara', 'Quadro formaggi', 'Capriciosa', 'Con Frutti di Mare']
friend_pizza = my_pizza[:]
my_pizza.append('Mergerita')
friend_pizza.append('Quadro stagioni')
print(my_pizza)
print(friend_pizza)
# ['Carbonara', 'Quadro formaggi', 'Capriciosa', 'Con Frutti di Mare', 'Mergerita']
# ['Carbonara', 'Quadro formaggi', 'Capriciosa', 'Con Frutti di Mare', 'Quadro stagioni']

# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.
# ?????????

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

foods = ('pizza', 'falafel', 'carrot cake', 'cheescacke', 'ice cream')
for food in foods:
	print(food)
# foods[3] = 'cartofele prajitele'

foods = ('pizza', 'falafel', 'carrot cake', 'cheescacke', 'cartofele')
print(foods)




