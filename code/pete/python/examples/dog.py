# use the class keyword to define a class
# no def, no ()
# snake_case is used most of the time in python
# PascalCase is used for class definitions
class Dog:
	bark_dict = {
		'small': 'yip',
		'medium': 'bark',
		'large': 'woof'
	}
	# class methods look like functions
	# the init method is a special dunder (double underscore)
	# method called when initializing or instantiating an object
	# an object is an instance of a class
	def __init__(self, name, age, breed, size):
		# the params above are passed in when the object is instantiated
		self.name = name
		self.age = age
		self.breed = breed
		self.size = size
	
	# self is the first param to every method in a class
	def get_info(self):
		# commented out print is a side effect
		# nothing wrong with having a print statemnt in a method,
		# but there's a lot more that can be done with the returned f-string
		# print(f'name: {self.name}\nage: {self.age} years\nbreed: {self.breed}\nsize: {self.size}')
		return f'name: {self.name}\nage: {self.age} years\nbreed: {self.breed}\nsize: {self.size}'
		
	def bark(self):
		print(self.bark_dict[self.size])
		# print('woof')

	# dunder or magic methods run automatically in certain instances
	def __str__(self):
		return self.name


# instantiation: making an instance (object) of a class
bolt = Dog('Bolt', 1.5, 'Husky', 'medium')
# bolt.size
print(bolt)
bolt_info = bolt.get_info()
print(bolt_info)
bolt.bark()

print()
pax = Dog('Pax', 9, 'Greyhound', 'large')
print(pax)
pax_info = 'Info about Pax:\n' + pax.get_info()
print(pax_info)
pax.bark()

print()
luna = Dog('Luna', 5, 'Some kind of sheepdog', 'small')
print(luna)
print(luna.get_info())
luna.bark()

# super_number = 1 + '2'
super_dog = bolt + pax + luna
print(super_dog)











# def return_hello():
# 	return 'hello'

# print(return_hello())
# print(return_hello())