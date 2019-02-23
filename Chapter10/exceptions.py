try:
	print(5/1)
except ZeroDivisionError:
	print('You can\'t devide by zero')
else:
	print('This is not like final block in Java')

# If file will not exist anymore, download it from (http://gutenberg.org/)
alice = '/Users/Aleksandra/Documents/programming/Python/PythonFromScratch/pcc/chapter_10/alice.txt'

try:
	with open(alice) as file_alice:
		words = file_alice.read().split()
		print(words.count('Alice'))
		print(words.count('the'))
		num_words = len(words)
		print(num_words)
except FileNotFoundError:
	print('Sorry, the file ' + alice + ' does not exist.')



def count_words(file):
	"""Count the approximate number of words in a file."""
	try:
		with open(file) as file_obj:
			content = file_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + file + "does not exist."
		print(msg)
	else:
		words = content.split()
		return len(words)

moby_dick = '/Users/Aleksandra/Documents/programming/Python/PythonFromScratch/pcc/chapter_10/moby_dick.txt'

print(count_words(moby_dick))























