#!/usr/bin/env python

"""
	Unit Testing Simple Math Functions
	https://docs.python.org/3/library/unittest.html#assert-methods
"""

# Imports
import unittest
import calc

# Docs
__author__ = 'Vaux Gomes'
__version__ = '1.0.0'

#
class TestMath(unittest.TestCase):
	"""Unit Testing"""

	#
	def test_add(self):
		"""Testing add function"""
		self.assertEqual(calc.add(1,1), 2)
		self.assertEqual(calc.add(1,-1), 0)
		self.assertEqual(calc.add(-1,-1), -2)
		self.assertEqual(calc.add(-1,0), -1)

	#
	def test_sub(self):
		"""Testing add function"""
		self.assertEqual(calc.sub(1,1), 0)
		self.assertEqual(calc.sub(1,-1), 2)
		self.assertEqual(calc.sub(-1,-1), 0)
		self.assertEqual(calc.sub(-1,0), -1)

	#
	def test_mul(self):
		"""Testing add function"""
		self.assertEqual(calc.mul(1,1), 1)
		self.assertEqual(calc.mul(1,-1), -1)
		self.assertEqual(calc.mul(-1,-1), 1)
		self.assertEqual(calc.mul(-1,0), 0)


	def test_div(self):
		"""Testing add function"""
		self.assertEqual(calc.div(1,1), 1)
		self.assertEqual(calc.div(1,-1), -1)
		self.assertEqual(calc.div(-1,-1), 1)
		
		#
		with self.assertRaises(ValueError):
			calc.div(1, 0)

#
if __name__ == "__main__":
	"""Main function"""
	unittest.main()
