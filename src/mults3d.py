from numpy import array

def sixthroot(x, y):
	"""
	6th root of unity-complex multiplication
	i**2 = -j, j**2 = -i, ij = 1
	(a + bi + cj)(d + ei + fj)
		=	ad  + aei + afj
			bdi - bej + bf
			cdj + ce  - cfi
	"""
	a,b,c = x
	d,e,f = y
	return array((a*d + b*f + c*e,
				  b*d + a*e - c*f,
				  c*d + a*f - b*e))

def mut_complex(x, y):
	"""Mutually complex multiplication"""
	a,b,c = x
	d,e,f = y
	return array((a*d - b*f - c*e,
				  b*e + a*e + c*f,
				  c*f + a*f + b*e))

def mut_split(x, y):
	"""Mutually split-complex multiplication"""
	a,b,c = x
	d,e,f = y
	return array((a*d + b*f + c*e,
				  b*e + a*e + c*f,
				  c*f + a*f + b*e))

def double_complex(x, y):
	"""Doubly complex multiplication"""
	a,b,c = x
	d,e,f = y
	return array((a*d - b*f - c*e,
				  b*e + a*e - c*f,
				  c*f + a*f - b*e))

def anti_part_assoc(x, y):
	a,b,c = x
	d,e,f = y
	return array((a*d + b*f - c*e,
				  b*e + a*e + c*f,
				  c*f + a*f + b*e))

def anti_nonassociative(x, y):
	a,b,c = x
	d,e,f = y
	return array((a*d + b*f - c*e,
				  b*e + a*e - c*f,
				  c*f + a*f - b*e))

def anti_part_assoc_neg(x, y):
	a,b,c = x
	d,e,f = y
	return array((a*d + b*f - c*e,
				  b*e + a*e + c*f,
				  c*f + a*f - b*e))

def vect_shuffle(x, y):
	"""Shuffling pointwise multiplication"""
	a,b,c = x
	d,e,f = y
	return array((b*e, c*f, a*d))

def vect_shuffle_neg1(x, y):
	"""Shuffling pointwise multiplication. One negative"""
	a,b,c = x
	d,e,f = y
	return array((-b*e, c*f, a*d))

def vect_shuffle_neg2(x, y):
	"""Shuffling pointwise multiplication. Two negatives"""
	a,b,c = x
	d,e,f = y
	return array((b*e, -c*f, -a*d))

def shuffle_nonassoc(x, y):
	"""
	Nonassociative multiplication: shuffle as above, but with
	ij = k, ik = j, jk = i
	"""	
	a,b,c = x
	d,e,f = y
	return array((c*e + c*f + b*f, b*d + b*e + a*e, a*d + c*d + a*f))

def shuffle_nonassoc_neg(x, y):
	"""
	Nonassociative multiplication 2: same as above, but shuffling (i^2, etc)
	has opposite sign of combining (ij, etc)
	"""	
	a,b,c = x
	d,e,f = y
	return array((c*e - c*f + b*f,
				  b*d - b*e + a*e,
				 -a*d + c*d + a*f))
