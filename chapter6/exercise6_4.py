person = {
	'first_name' : 'Mob',
	'last_name'  : 'Murnquist',
	'age'        :  37,
	'city'       : 'Meatac'}

for k, v in person.items():
	print(f'{k} : {v}')

fave_nums = {
	'Person1' : 42,
	'Person2' : 7,
	'Person3' : 8,
	'Person4' : 13,
	'Person5' : 3
}

for person in fave_nums.values():
	print(person)

glossary = {
	'simulacrum'   : 'An image or representation of someone or something',
	'appanage'     : 'A necessary accompaniment',
	'deliquescent' : 'Becoming liquid, or having a tendency to become liquid.',
	'quondom'      : 'That was once; former',
	'corybantic'   : 'wild; frenzied'
}

for word, meaning in glossary.items():
	print(f'{word} : \n{meaning}')

rivers = {
	'nile'        : 'egypt',
	'yangtze'       : 'china',
	'mississippi' : 'united states'
}

for river, country in rivers.items():
	print(f'The {river.title()} River runs through {country.title()}')
for river in rivers.keys():
	print(river)
for river in rivers.values():
	print(river)

poll = {
	'Jessica' : 'Python',
	'Maxwell' : 'C++',
	'Lisa'    : 'Javascript',
	'Miranda' : 'Java',
	'Kanye'   : 'Python'
}

names = ['Jessica', 'Miranda', 'Lyse', 'Marik']

for name in names:
	print(f'\nHello, {name}.')
	if name in poll:
		print(f'{name}, thank you for voting.')
	else:
		print(f'{name}, please enter your vote.')