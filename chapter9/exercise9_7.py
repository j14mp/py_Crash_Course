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

class Admin(User):
	def __init__(self, first_name, last_name, age, eye_color):
		super().__init__(first_name, last_name, age, eye_color)
		self.privileges = Privileges()

class Privileges():
	def __init__(self):
		self.privileges = [
		'can add post',
		'can delete post',
		'can ban user',
		'can change username']	

	def show_privileges(self):
		print('This admin can do the following: ')
		print(self.privileges)

discord_mod = Admin('Tom', 'Balom', 28, 'brown')
discord_mod.privileges.show_privileges()