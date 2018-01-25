# x** 2 - возведение в квадрат
f = lambda x: x**2
print(f(3))

print((lambda x: x**2)(9))

print((lambda x,y: x + y)(4,3))

def func(a):
	a = a * 2
	def FuncInFunc(y):
		return a + y
	return FuncInFunc

print(func(10)(2))

def func2(x):
	x = x * 2
	return lambda y: x + y

print(func2(10)(2))