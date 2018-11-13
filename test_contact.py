#!/usr/bin/env python

"""Unit Testing Sample Class"""

# Imports
import unittest
from contact import Contact

# Docs
__author__ = 'Vaux Gomes'
__version__ = '1.0.0'

#
class TestMath(unittest.TestCase):
	"""Unit Testing"""

	#
	def setUp(self):
		self.contact = Contact('name', 'SURNAME', 'EnterPRISE', '+55 99 99999 9999')

	#
	def tearDown(self):
		pass

	#
	def test_init(self):
		"""Init test"""
		self.assertEqual(self.contact.name, 'Name')
		self.assertEqual(self.contact.surname, 'Surname')
		self.assertEqual(self.contact.comp, 'Enterprise')
		self.assertEqual(self.contact.number, '+55 99 99999 9999')

	#
	def test_email(self):
		"""Email test"""
		self.assertEqual(self.contact.email(), 'name.surname@enterprise.com')

	#
	def test_card(self):
		"""Card test"""
		self.assertEqual(self.contact.card(), 'SURNAME, Name (+55 99 99999 9999)')

	#
	def test_card(self):
		"""Card test"""
		self.contact.set_number(123)
		self.assertEqual(self.contact.number, '123')
		self.assertIsInstance(self.contact.number, str)

#
if __name__ == "__main__":
	"""Main function"""
	unittest.main()
