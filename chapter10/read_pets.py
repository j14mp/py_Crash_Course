"""
Checks to see if txt file exists. If not, throws silent exception
"""

def list_pets(filename):
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		print(contents)

list_pets('cats.txt')
list_pets('dogs.txt')