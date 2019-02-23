pi_digits = '/Users/Aleksandra/Documents/programming/Python/PythonFromScratch/pcc/chapter_10/pi_digits.txt'

pi_million_digits = '/Users/Aleksandra/Documents/programming/Python/PythonFromScratch/pcc/chapter_10/pi_million_digits.txt'



with open(pi_digits) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

with open(pi_digits) as file_object:
	for line in file_object:
		print(line.rstrip())

# with open('applesAlina.jpg') as file_object:
# 	lines = file_object.readlines()
# for line in lines:
# 	print(line.rstrip())
with open(pi_million_digits) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string +=line.strip()
print(pi_string[:51] + "...")
print(len(pi_string))

birthday = '200489'
if birthday in pi_string:
	print("Your birthday appears")
else:
	print("It doesnt!!!")

message = "I really like dogs."
message = message.replace('dog', 'cat')
print(message)






