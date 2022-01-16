print('\nEnter q to quit.')

with open('guest_book.txt', 'a') as file_object:
	username = ''
	while username != 'q':
		username = input('What is your name? ')
		if username == 'q':
			break
		else:
			print(f'Your name is {username}. Welcome!\n')
			file_object.write(f'{username} has written their name in the guest book.\n')
