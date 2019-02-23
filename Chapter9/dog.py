class Dog():

	def __init__(self, name, age):
		self.name = name
		self.age = age


	def sit(self):
		print(self.name.title() + " is sitting now.")


	def roll_over(self):
		print(self.name.title() + " rolled over!")


	def set_age(self, age):
		self.age = age


class Dvorniaga(Dog):

	def __init__(self, name, age):
		super().__init__(name, age)


my_dog = Dvorniaga('Kuzea', 13)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.set_age(4)
print(my_dog.age)