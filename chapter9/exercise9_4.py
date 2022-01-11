class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0 

	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restaurant(self):
		print('The restaurant is now open!')

	def increment_number_served(self, number_of_people):
		self.number_served += number_of_people

	def new_day(self):
		self.number_served = 0
		print(f'It is the beginning of a new day.')
		print(f'The number of people served is now {self.number_served}')


restaurant = Restaurant('Duranys', 'Greek')
print(f'This restaurant has served {restaurant.number_served} people.')
restaurant.increment_number_served(20)
print(f'This restaurant has served {restaurant.number_served} people.')
restaurant.increment_number_served(11)
print(f'This restaurant has served {restaurant.number_served} people.')
restaurant.new_day()