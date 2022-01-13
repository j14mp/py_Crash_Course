from random import randint

class Die():
	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self, num_of_rolls = 1):
		print(f'Rolling dice {num_of_rolls} times: ')
		for n in range(0, num_of_rolls):
			roll = randint(1, self.sides)
			print(f'You rolled a {roll}.')
			if roll == 21:
				print('Critical hit!')
			elif roll == 1:
				print('Total failure!')

standard = Die(21)

standard.roll_die(10)