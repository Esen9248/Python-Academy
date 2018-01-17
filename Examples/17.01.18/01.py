def hello():
	x = 1
	def f1():
		y = 2
		print('f1', x , y)

	def f2():
		z = 3
		print('f2', x, z)
	f1()
	print('Hello World', x)
	f2()

hello()