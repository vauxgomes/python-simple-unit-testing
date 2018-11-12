#!/usr/bin/env python

"""Simple Math Functions"""

# Docs
__author__ = 'Vaux Gomes'
__version__ = '1.0.0'


def add(x, y):
	"""Adds two numbers"""
	return x + y


def sub(x, y):
	"""Subtracts two numbers"""
	return x - y


def mul(x, y):
	"""Multiplies two numbers"""
	return x * y


def div(x, y):
	"""Divides two numbers"""
	if y == 0:
		raise ValueError('Cannot divide by zero (0).')

	return x / y