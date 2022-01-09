def city_country(city, country):
	return f'{city.title()}, {country.title()}'

print(city_country('london', 'england'))
print(city_country('seattle', 'united states'))
print(city_country('geneva', 'switzerland'  ))

def make_album(artist, title, num_of_songs = None):
	if num_of_songs:
		return {'artist' : artist, 'title' : title, 'num_of_songs' : num_of_songs}
	else:
		return {'artist' : artist, 'title' : title}

print(make_album('Kanye', 'Life of Pablo'))
print(make_album('Stormzy', 'Heavy is the Head'))
print(make_album('Kanye', '808', 12))

while True:
	print('\nEnter q to quit at any time.')
	print("\nPlease enter the artist's name: ")
	artist_name = input('artist: ')
	if artist_name == 'q':
		break
	print("Please enter the album name: ")
	album_name = input('album: ')
	if album_name == 'q':
		break

	print('An album has been created:')
	print(make_album(artist_name, album_name))
