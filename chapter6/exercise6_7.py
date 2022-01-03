people = [
	{
	'name' : 'Urianger',
	'race' : 'Elezen',
	'class' : 'astrologian',
	'location' : 'Il Mheg'
	},
	{
	'name' : 'Alphinaud',
	'race' : 'Elezen',
	'class': 'scholar',
	'location' : 'Kholusia'
	},
	{
	'name' : 'Crystal Exarch',
	'race' : 'Miqote',
	'class' : 'all-rounder',
	'location' : 'the Crystarium'
	}
]


for person in people:
	print(f"This is {person['name']}. They are a {person['race']} "
		  f"{person['class']}, and they are currently in {person['location']}")


busky = {
	'name' : 'Busky',
	'breed': 'Husky',
	'owner': 'Jeff'
}

linko = {
	'name' : 'Linko',
	'breed': 'Dachshund',
	'owner': 'Zelda'
}

dolla = {
	'name' : 'Dolla',
	'breed' : 'Dalmatian',
	'owner' : 'Firefighter'
}

pets = [busky, linko, dolla]
for pet in pets:
	print(pet)

cities = {
	'Tokyo' : {
		'country' : 'Japan',
		'population' : '14 million',
		'fact' : 'there is one vending machine per 24 people in Japan.'
	},
	'Tel Aviv' : {
		'country' : 'Israel',
		'population' : '435 thousand',
		'fact' : 'Tel Aviv has 300 annual days of sunshine.'
	},
	'Mecca' : {
		'country' : 'Saudi Arabia',
		'population' : '1.5 million',
		'fact' : 'only muslims are allowed in Mecca.'
	}
}

for city, info in cities.items():
	print(f"\nWelcome to {info['country']}!")
	print(f"This is {city}, population: {info['population']}.")
	print(f"One interesting fact is that {info['fact']}")
	