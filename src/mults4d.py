from numpy import array

def quaternion(x, y):
	"""
	Quaternion multiplication
	Anticommutative
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f - c*g - d*h
				 ,a*f + b*e + c*h - d*g
				 ,a*g + c*e + d*f - b*h
				 ,a*h + d*e + b*g - c*f))

def dihedral(x, y):
	"""
	Dihedral multiplication
	Anticommutative
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f + c*g + d*h
				 ,a*f + b*e + c*h - d*g
				 ,a*g + c*e - d*f + b*h
				 ,a*h + d*e - b*g + c*f))

def eighth(x, y):
	"""
	8th root of unity multiplication. j = sqrt i, k = -sqrt i
	Commutative, nonassociative in ij, ik
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f + c*h + d*g
				 ,a*f + b*e + c*g - d*h
				 ,a*g + c*e + d*f + b*h
				 ,a*h + d*e - b*g - c*f))

def squarerot(x, y):
	"""
	Square rotation symmetry multiplication. j^2 = k^2 = ijk = i, i^2 = 1
	Commutative
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e + b*f + c*h + d*g
				 ,a*f + b*e + c*g + d*h
				 ,a*g + c*e + d*f + b*h
				 ,a*h + d*e + b*g + c*f))

def triple_splitcomplex(x, y):
	"""
	Triply split-complex: i^2 = j^2 = k^2 = ijk = 1
	Commutative, Nonassociatve in i^2j
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e + b*f + c*g + d*h
				 ,a*f + b*e + d*g + c*h
				 ,a*g + c*e + d*f + b*h
				 ,a*h + d*e + b*g + c*f))

def triple_complex(x, y):
	"""
	Triply complex: i^2 = j^2 = k^2 = -1; ijk = 1
	Commutative, nonassociative in i^2j
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f - c*g - d*h
				 ,a*f + b*e + d*g + c*h
				 ,a*g + c*e + d*f + b*h
				 ,a*h + d*e + b*g + c*f))

def split_complex_double_complex(x, y):
	"""
	Complex in i, j; split-complex in k. ij = -k
	Commutative, nonassociative in jk^2
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f - c*g + d*h
				 ,a*f + b*e + d*g + c*h
				 ,a*g + c*e + d*f + b*h
				 ,a*h + d*e - b*g - c*f))

def complex_double_split_complex(x, y):
	"""
	Complex in i; split-complex in j, k. ik = j, ij = k, jk = -i
	Commutative, nonassociative in ij^2
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f + c*g + d*h
				 ,a*f + b*e - d*g - c*h
				 ,a*g + c*e + d*f + b*h
				 ,a*h + d*e + b*g + c*f))

def antidihed(x, y):
	"""
	Split-dihedral multiplication. i^2 = ijk = 1; j^2 = k^2 = -1
	Commutative, nonassociative in ik^2
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e + b*f - d*h - c*g
				 ,a*f + b*e + d*g + c*h
				 ,a*g + c*e - d*f - b*h
				 ,a*h + d*e - b*g - c*f))

def antieighth(x, y):
	"""
	Anti-8th root of unity multiplication. i^2 = -1, j^2 = k^2 = i
	Anticommutative, nonassociative in j^2k
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e - b*f + c*h - d*g
				 ,a*f + b*e + c*g + d*h
				 ,a*g + c*e + d*f - b*h
				 ,a*h + d*e + b*g - c*f))

def negi_dihedral(x, y):
	"""
	Negi-dihedral ; i^2 = ijk = 1, j^2 = k^2 = 1
	Anticommutative, nonassociative
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e + b*f - c*g - d*h
				 ,a*f + b*e - d*g + c*h
				 ,a*g + c*e - d*f + b*h
				 ,a*h + d*e + b*g - c*f))

def negi_quaternion(x, y):
	"""
	Negi-quaternion multiplication
	Anticommutative, nonassociative in i^2j
	"""
	a,b,c,d = x
	e,f,g,h = y
	return array((a*e + b*f + c*g + d*h
				 ,a*f + b*e + c*h - d*g
				 ,a*g + c*e + d*f - b*h
				 ,a*h + d*e + b*g - c*f))
