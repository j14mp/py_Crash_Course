def city_and_country(city, country, population = ''):
	if population:
		place = f'{city}, {country} - population {population}.'
	else:
		place = f'{city}, {country}'
	place = place.title()
	return place
