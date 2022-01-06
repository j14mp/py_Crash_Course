sub_orders = ['meatball', 'pastrami', 'tuna', 'veggie', 'pastrami', 'steak', 'chicken', 'pastrami']
finished_subs = []

while sub_orders:
	finished_sub = sub_orders.pop()
	if finished_sub != 'pastrami':
		print(f'I made your {finished_sub} sub.')
		finished_subs.append(finished_sub)
	else:
		print('We are all out of pastrami! Sorry!')

if finished_subs:
	print('\nThese subs were made: ')
	for sub in finished_subs:
		print(sub)

polling_active = True

results = {}
while polling_active:
	name = input('\nWhat is your name? ')
	vacation = input('Where would you like to stay? ')

	results[name] = vacation

	again = input('Would you like to continue the poll? yes/no ')
	if again == 'yes':
		continue
	elif again == 'no':
		polling_active = False


print('\n-----Poll Results-----\n')
for name, result in results.items():
	print(f'{name} would like to go to {result}')


