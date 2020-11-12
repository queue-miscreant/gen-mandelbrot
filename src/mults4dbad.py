#a collection of "bad" 4d multiplication schemes, which I
#haven't completely organized
from numpy import array
 
def mult_part_complex(x, y):
	"""
	Part complex, part doubly complex
	Nonassociative
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f + c*g + d*h
				 ,a*f + b*e + d*g + c*h
				 ,a*g + c*e + d*f + b*h
				 ,a*h + d*e + b*g + c*f))

def mult_part_complex2(x, y):
	"""
	Part2 complex, part doubly complex
	Nonassociative
	"""
	a,b,c,d = x
	e,f,g,h = y
	return np.array((a*e + b*f - c*g - d*h
					,a*f + b*e + d*g + c*h
					,a*g + c*e + d*f + b*h
					,a*h + d*e + b*g + c*f))

def mult_part_complex_same(x, y):
	"""
	Matching signs of i^2, jk, kj
	"""
	a,b,c,d = x
	e,f,g,h = y
	return np.array((a*e - b*f + c*g + d*h
					,a*f + b*e - d*g - c*h
					,a*g + c*e + d*f + b*h
					,a*h + d*e + b*g + c*f))

def mult_part_complex_opposite(x, y):
	"""
	Opposite signs of i^2, and jk, kj
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f + c*g + d*h
				 ,a*f + b*e + d*g + c*h
				 ,a*g + c*e - d*f - b*h
				 ,a*h + d*e - b*g - c*f))

def mult_part_complex_half(x, y):
	"""
	Half same signs of i^2, jk, kj, with additional negative
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f + c*g + d*h
				 ,a*f + b*e - d*g - c*h
				 ,a*g + c*e - d*f - b*h
				 ,a*h + d*e + b*g + c*f))

def mult_part_complex_split_half(x, y):
	"""
	Negi same signs of i^2, jk, kj, opposite to j^2 and k^2
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f + c*g + d*h
				 ,a*f + b*e - d*g - c*h
				 ,a*g + c*e - d*f - b*h
				 ,a*h + d*e - b*g - c*f))

def mult_part_double_complex_half(x, y):
	"""
	Negiopp signs of i^2, j^2, jk, kj, opposite to k^2
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f - c*g + d*h
					,a*f + b*e - d*g - c*h
					,a*g + c*e - d*f - b*h
					,a*h + d*e - b*g - c*f))
