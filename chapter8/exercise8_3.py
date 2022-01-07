def make_shirt(size = 'large' , message = 'I love Python'):
 print(f'You have ordered a size {size} shirt, with a message to be printed on: \"{message}\"')

make_shirt('medium', 'Veni Vidi Vici')
make_shirt(size = 'large', message = 'Oopsie woopsie uwu')
make_shirt()

def describe_city(city, country = 'the United States'):
	print(f'{city} is in {country}.')

describe_city('Seattle')
describe_city('Boston')
describe_city('Tokyo', country = 'Japan')
