"""
Program to practice throwing exceptions
"""
while True:
	print('\nEnter q to quit. ')
	try:
		first_num = input('Enter a number: ')
		if first_num == 'q':
			break
		first_num = int(first_num)
		second_num = input('Enter another number: ')
		if second_num == 'q':
			break
		second_num = int(second_num)
		print('Adding numbers...')
	except ValueError:
		print('One of your numbers was not a number. Please try again.')
	else:
		answer = first_num + second_num
		print(f'{first_num} plus {second_num} equals {answer}.')
