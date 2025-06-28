import pytest

def test_calc_addition():
	# function test the output of 2 + 4
	output = 2 + 4
	assert output == 6

def test_calc_substraction():
	# function test the output of 2 - 4
	output = 2 - 4
	assert output == -2

def test_calc_multiply():
	# function test the output of 2 * 4
	output = 2 * 4
	assert output == 8

def test_coucou():
	# function test if the output returns 'hello'
	output = 'hello'
	assert output == 'hello'
