class Geometry(object):
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def perimeter(self):
		P = 2*(self.a+self.b)
		return P

	def area(self):
		S = self.a*self.b
		return S

class Rectangle(Geometry):
	pass

class Square(Rectangle):
	def __init__(self,a):
		super(Square, self).__init__(a, a)

class Triangle(Geometry):
	def __init__(self,a,b,c,h):
		self.c = c
		self.h = h
		super(Triangle, self).__init__(a,b)

	def perimeter(self):
		P = self.a+self.b+self.c
		return P

	def area(self):
		S = (self.a/2)*self.h
		return S

class Circle(Geometry):
	def __init__(self,r):
		self.r = r

	def perimeter(self):
		P = self.r*(3.14*2)
		return P

	def area(self):
		S = 3.14*(self.r**2)
		return S

if __name__ == '__main__':
	a_rc, b_rc = [int(i) for i in input('Enter two sides of rectangle: ').split()]
	square_length = int(input('Enter a length of square: '))
	a_tr, b_tr, c_tr, h_tr = [int(i) for i in input('Enter three sides and a height of triangle: ').split()]
	r_cr = int(input('Enter a radius of circle: '))

	rectangle = Rectangle(a_rc, b_rc)
	square = Square(square_length)
	triangle = Triangle(a_tr, b_tr, c_tr, h_tr)
	circle = Circle(r_cr)

	print('')
	print('Perimeter of rectangle is {}, area of rectangle is {}'.format(rectangle.perimeter(), rectangle.area()))
	print('Perimeter of square is {}, area of square is {}'.format(square.perimeter(), square.area()))
	print('Perimeter of triangle is {}, area of triangle is {}'.format(triangle.perimeter(), triangle.area()))
	print('Perimeter of circle is {}, area of circle is {}'.format(circle.perimeter(), circle.area()))
