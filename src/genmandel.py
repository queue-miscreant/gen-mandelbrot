import time
from itertools import product
from functools import reduce

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
import mults2d as d2
import mults3d as d3
import mults4d as d4

def get_grid(points, lower=-2, upper=2, unityroot=1j):
	'''
	Generate square numpy array of complex numbers from `lower` to `upper`
	with `points`^2 test points
	'''
	test_range = np.linspace(lower, upper, points)
	real = np.array([test_range for _ in range(points)])
	imag = np.array([test_range[::-1] for _ in range(points)])
	return real + unityroot*imag.T

def mandelbrot(iters, unityroot=4, pow=2, thresh=4):
	'''Classical mandelbrot set with normal complex arithmetic'''
	root = np.exp(np.pi * 2j / unityroot)
	zs = get_grid(200, unityroot=root)
	c = zs.copy()
	small = np.zeros(zs.shape)
	for _ in range(iters):
		zs = zs**pow + c
		small += (abs(zs) >= thresh)
	return small

norm2 = lambda x: sum(map(lambda i: i**2, x))
norm2.__doc__ = "$a^2 + b^2$"
relnorm = lambda x: sum(map(lambda i: ((-1)**i[0])*(i[1]**2), enumerate(x)))**2
relnorm.__doc__ = "$(a^2 - b^2)^2$"
relnorm2 = lambda x: (reduce(lambda a,b: a*b, x))**2
relnorm2.__doc__ = "$(ab)^2$"

taxicab = lambda x: sum(map(abs, x))
taxicab.__doc__ = "$|a| + |b|$"
maxnorm = lambda x: max(map(abs, x))
maxnorm.__doc__ = "$\\max(|a|, |b|)$"

def gen_mandelbrot(points, iters, mult=d2.comp, norm=norm2, pow=2, thresh=4):
	'''
	Generalized mandelbrot set.
	`mult` describes the multiplication
	`norm` describes the norm to check against `thresh`
	z^n can be changed with `pow`.
	'''
	plane = get_grid(points, -2, 2)
	zs = np.array([np.array((i.real, i.imag)) for i in plane.flatten()])
	c = zs.copy()

	#bleh, efficiency
	power = lambda x: reduce(mult, [x for _ in range(pow)])
	#power = lambda x: reduce(mult, [x for _ in range(pow)]) if norm(x) < thresh else x

	small = np.zeros(len(c))

	for i in range(iters):
		tick = time.time()
		zs = np.apply_along_axis(power, 1, zs) + c
		print(f"Iteration {i}; time = " + str(time.time() - tick))
		small += np.apply_along_axis(norm, 1, zs) >= thresh

	return np.reshape(small, plane.shape)

def shownorms(points, iters, mult, norms=None, thresh=8, shape=None):
	if norms is None:
		norms = (norm2, relnorm, taxicab, maxnorm)
	if shape is None:
		shape = [2,2]

	for i, norm in enumerate(norms):
		plt.subplot(*shape, i+1)
		plt.title(norm.__doc__)
		plt.imshow(gen_mandelbrot(points, iters, mult, norm, thresh=thresh), cmap="inferno")

def mandelbrotn(points, iters, mult=d3.sixthroot, norm=norm2, pow=2, thresh=6, d=3):
	'''
	Apply mandelbrot transformation to n-dimensional points
	`points`^3 comprise the lattice, and it is applied `iters` times

	Only returns points that lie in the set.
	'''
	zs = np.array([np.array(i)
		for i in product(list(np.linspace(-2, 2, points)), repeat=d)])
	c = zs.copy()
	small = np.zeros(len(zs))

	power = lambda x: reduce(mult, [x for _ in range(pow-1)], x)

	for i in range(iters):
		tick = time.time()
		zs = np.apply_along_axis(power, 1, zs) + c
		print(f"Iteration {i}; time = " + str(time.time() - tick))
		small += np.apply_along_axis(norm, 1, zs) >= thresh

	return c[small == 0]

def slice3d(points, iters, a=0, mult=d3.sixthroot, norm=norm2, pow=2, thresh=12):
	'''
	Get a slice in the ij plane of the above, where a=`a`
	`points`^3 comprise the lattice, and it is applied `iters` times

	Returns the number of iterations the point has a 2-norm larger than `thresh`
	'''
	plane = get_grid(points)
	zs = np.array([np.array((a, i.real, i.imag)) for i in plane.flatten()])
	c = zs.copy()

	#bleh, efficiency
	#power = lambda x: reduce(mult, [x for _ in range(pow)])
	power = lambda x: reduce(mult, [x for _ in range(pow)]) if norm(x) < thresh else x

	small = np.zeros(len(c))

	for i in range(iters):
		tick = time.time()
		zs = np.apply_along_axis(power, 1, zs) + c
		print(f"Iteration {i}; time = " + str(time.time() - tick))
		small += np.apply_along_axis(norm, 1, zs) >= thresh

	return np.reshape(small, plane.shape)

def scatter3(array, subplot, title, i=0, j=None, k=None, **kwargs):
	'''3D scatterplot of `array` for use with mandelbrot3'''
	ret = plt.subplot(subplot, projection="3d")
	plt.title(title)
	if j is None:
		j = i+1
	if k is None:
		k = j+1
	ret.scatter(array[:,i], array[:,j], array[:,k], **kwargs)
	ret.xaxis.label.set_text("1")
	ret.yaxis.label.set_text("i")
	ret.zaxis.label.set_text("j")
	return ret

default_order = lambda x, y, a, b: (x, y, a, b)
partial_vector_order = lambda x, y, a, b: (a, x, y, b)
vector_order = lambda x, y, a, b: (b, a, x, y)
dihedral_order = lambda x, y, a, b: (a, b, x, y)

def slice4d(points, iters, a=0, b=0, mult=d4.quaternion, pow=2, thresh=16, order=default_order):
	'''
	4D mandelbrot set slicer, where a and b control the two other components
	'''
	plane = get_grid(points)
	zs = np.array([np.array(order(i.real, i.imag, a, b)) for i in plane.flatten()])
	c = zs.copy()

	#bleh, efficiency
	power = lambda x: reduce(mult, [x for _ in range(pow)])
	#power = lambda x: reduce(mult, [x for _ in range(pow)]) if norm(x) < thresh else x

	small = np.zeros(len(c))

	for i in range(iters):
		tick = time.time()
		zs = np.apply_along_axis(power, 1, zs) + c
		print(f"Iteration {i}; time = " + str(time.time() - tick))
		small += np.apply_along_axis(norm2, 1, zs) >= thresh

	return np.reshape(small, plane.shape)

_slicer3 = lambda points, iters, a: slice3d(points, iters, a)
_slicer4 = lambda points, iters, a: slice4d(points, iters, a)

def slice_vid(as_, points, slicer=_slicer3, iters=7, fname="slices of 3d.mp4"):
	'''Generate a 3D slicing video'''
	writer = FFMpegWriter(fps=4)
	fig = plt.figure()
	with writer.saving(fig, fname, 144):
		for a in as_:
			slice_ = slicer(points, iters, a)
			plt.imshow(slice_, cmap='inferno')
			plt.clim(0, iters-1)
			plt.title(f"$\\Re(z) = {a}$")
			writer.grab_frame()
			plt.clf()
	print("\a")

			#xi = np.exp(1j * a)
			#x = points//2
			#plt.arrow(x, x, x//8*xi.real, -x//8*xi.imag, color="blue", width=0.25)
			#plt.title(f"$i^2 = {xi}$")

def all_slices(as_, points, mult, iters=7):
	'''
	For all the orderings given, generate slicings of a 4D set along subspaces
	where the final coordinate is 0
	'''
	for order, name in zip((default_order, partial_vector_order, vector_order, dihedral_order),
		("1", "j", "ijk", "1jk")):
		docstring = mult.__doc__.split(' ')[0].strip()
		slicer = lambda points, iters, a: slice4d(points, iters, a, mult=mult, order=order)
		slice_vid(as_, points, slicer, iters=iters, fname=f"slices {docstring} {name}.mp4")
