from random import choice

lotto = (1,2,3,4,5,6,7,8,
		'a','b','c','d','e')

winning_combo = []
for n in range(0, 4):
	winning_combo.append(choice(lotto))

print(f'The winning combination ticket is {winning_combo}')

my_ticket = [5, 'a', 'd', 8]

times_drawn = 0
while my_ticket != winning_combo:
	times_drawn += 1
	winning_combo = []
	for n in range(0, 4):
		winning_combo.append(choice(lotto))

print(f'It took {times_drawn} draws to get your ticket')



