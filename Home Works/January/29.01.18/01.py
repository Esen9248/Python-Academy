class Geometry(object):
	def __init__(self):
		pass
	def perimeter_sq(self, a):
		P = 4*a
		return P
	def area_sq(self, a):
		S = a**2
		return S
	def perimeter_tr(self, a, b, c):
		P = a+b+c
		return P
	def area_tr(self, a, h):
		S = (a/2)*h
		return S
	def perimeter_cr(self, r):
		P = r*(3.14*2)
		return P
	def area_cr(self, r):
		S = 3.14*(r**2)
		return S
	def perimeter_rc(self, a, b):
		P = 2*(a+b)
		return P
	def area_rc(self,a,b):
		S = a*b
		return S
if __name__ == '__main__':
	my_obj = Geometry()

	square_length = int(input('Enter a length of square: '))
	a_tr, b_tr, c_tr = [int(i) for i in input('Enter three sides of triangle: ').split()]
	a_trn, h_tr = [int(i) for i in input('Enter a side and a heigth of triangle: ').split()]
	r_cr = int(input('Enter a radius of circle: '))
	a_rc, b_rc = [int(i) for i in input('Enter two sides of rectangle: ').split()]

	print('Perimeter of square is {}, area of square is {}'.format(my_obj.perimeter_sq(square_length), my_obj.area_sq(square_length)))
	print('Perimeter of triangle is {}, area of triangle is {}'.format(my_obj.perimeter_tr(a_tr, b_tr, c_tr),my_obj.area_tr(a_trn, h_tr)))
	print('Perimeter of circle is {}, area of circle is {}'.format(my_obj.perimeter_cr(r_cr), my_obj.area_cr(r_cr)))
	print('Perimeter of rectangle is {}, area of rectangle is {}'.format(my_obj.perimeter_rc(a_rc, b_rc), my_obj.area_rc(a_rc, b_rc)))