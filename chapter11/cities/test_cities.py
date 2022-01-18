import unittest
from city_functions import city_and_country
class city_country_test(unittest.TestCase):
	"""Tests for city_functions.py"""

	def test_city_country(self):
		city_country_pair = city_and_country('madrid', 'spain')
		self.assertEqual(city_country_pair, 'Madrid, Spain')

	def test_city_country_pop(self):
		city_country_pop = city_and_country('madrid', 'spain', 100000)
		self.assertEqual(city_country_pop, 'Madrid, Spain - Population 100000.')

if __name__ == '__main__':
	unittest.main()