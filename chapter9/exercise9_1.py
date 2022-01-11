mcdonalds = Restaurant('McDonalds', 'American')
wendys = Restaurant('Wendys', 'American')

mcdonalds.describe_restaurant()
wendys.describe_restaurant()

class User:
	def __init__(self, first_name, last_name, age, eye_color):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.eye_color = eye_color

	def describe_person(self):
		print(f'\nYour name is {self.first_name} {self.last_name}!')
		print(f'You are age {self.age} and have {self.eye_color} colored eyes.')

	def greet_user(self):
		print(f'Welcome home, {self.first_name} {self.last_name}.')

yohannes = User('Yohannes', 'Magumba', 22, 'brown')
yohannes.describe_person()
yohannes.greet_user()

steve = User('Steve', 'Pastrana', 54, 'green')
steve.describe_person()
steve.greet_user()

bailey = User('Bailey', 'Montana', 32, 'blue')
bailey.describe_person()
bailey.greet_user()

"""
"""
