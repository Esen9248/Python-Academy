class B(object):
	p = 'AAA'

	def __init__(self, n):
		self.name = n

if __name__ == '__main__':
	a = B('test')
	c = B('abc')

	print(a.name, a.p)
	print(c.name, c.p)

	B.p = 'qwe'

	print(a.name, a.p)
	print(c.name, c.p)

	c.p = 'This c'

	print(a.name, a.p)
	print(c.name, c.p)
