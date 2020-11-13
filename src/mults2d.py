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
				  b*c + a*d + b*d))

def neg_indeterminate(x, y):
	a,b = x
	c,d = y
	return array((a*c,
				  b*c + a*d - b*d))

def compmult_comp(alpha, x, y):
	a,b = x
	c,d = y
	alpha = complex(alpha)
	return array((a*c + b*d*alpha.real
				 ,a*d + b*c + b*d*alpha.imag))
