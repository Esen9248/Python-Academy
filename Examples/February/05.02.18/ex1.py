class A(object):
	def __init__(self, x, y, metrics='m'):
		self.x = x
		self.y = y
		self.metrics = 'm'

	def calc_area(self):
		return self.x * self.y

	@staticmethod
	def static_func(n):
		return n/2

	@classmethod
	def another_static_method(cls, x, y):
		return cls(x/2, y/2, 'km')

if __name__ == '__main__':
	x = A.static_func(6)
	print(x) # print(A.static_func(6))

	c = A.another_static_method(3, 4)
	print(c.calc_area())

	a = A(3, 2)
	print(a.calc_area())
