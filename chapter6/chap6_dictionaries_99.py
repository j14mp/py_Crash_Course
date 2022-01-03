person = {
    'first_name' : 'first',
	'last_name'  : 'last',
	'age'        :  27,
	'city'       : 'Seatac'}

print(person)

fave_nums = {
	'Person1' : 42,
	'Person2' : 7,
	'Person3' : 8,
	'Person4' : 13,
	'Person5' : 3
}

for person in fave_nums:
	print(fave_nums[person])

glossary = {
	'simulacrum'   : 'An image or representation of someone or something',
	'appanage'     : 'A necessary accompaniment',
	'deliquescent' : 'Becoming liquid, or having a tendency to become liquid.',
	'quondom'      : 'That was once; former',
	'corybantic'   : 'wild; frenzied'
}

for word in glossary:
	print(f'{word} : \n{glossary[word]}')
