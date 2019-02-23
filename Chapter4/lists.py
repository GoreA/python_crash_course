for numb in range(1,5):
	print(numb)
# Output
# 1
# 2
# 3
# 4

numbers = list(range(1,5))
print(numbers)
# [1, 2, 3, 4]

even_numbers = list(range(2, 11, 2))
print(even_numbers)
# [2, 4, 6, 8, 10]
odd_numbers = list(range(1, 11, 2))
print(odd_numbers)
# [1, 3, 5, 7, 9]

squares = []
for num in range(1, 11):
	squares.append(num**2)

print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

