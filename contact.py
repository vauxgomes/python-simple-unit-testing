#!/usr/bin/env python

"""Simple Class"""

# Docs
__author__ = 'Vaux Gomes'
__version__ = '1.0.0'

#
class Contact(object):
	"""Sample Contact class"""

	#
	def __init__(self, name, surname, comp, number):
		""" Constructor """
		self.name = name.title()
		self.surname = surname.title()
		self.comp = comp.title()
		self.number = str(number)

	#
	def fullname(self):
		"""Full Name"""
		return self.name + ' ' + self.surname

	#
	def email(self):
		"""Email"""
		return '{0}.{1}@{2}.com'.format(self.name, self.surname, self.comp).lower()

	#
	def card(self):
		"""Card"""
		return '{1}, {0} ({2})'.format(self.name, self.surname.upper(), self.number)

	#
	def set_number(self, number):
		"""Set Number"""
		self.number = str(number)