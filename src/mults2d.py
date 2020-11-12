from numpy import array

def comp(x, y):
	"""
	Complex number multiplication
	i**2 = -1
	(a + bi)(c + di) = (ac - bd) + (bc + ad)i
	"""
	a,b = x
	c,d = y
	return array((a*c - b*d, 
				  b*c + a*d))

def split(x, y):
	"""
	Splitcomplex number multiplication
	i**2 = 1
	(a + bi)(c + di) = (ac + bd) + (bc + ad)i
	"""
	a,b = x
	c,d = y
	return array((a*c + b*d,
				  b*c + a*d))

def indeterminate(x, y):
	a,b = x
	c,d = y
	return array((a*c,
				  b*c + b*d + a*d))

def neg_indeterminate(x, y):
	a,b = x
	c,d = y
	return array((a*c,
				  b*c + b*d - a*d))
