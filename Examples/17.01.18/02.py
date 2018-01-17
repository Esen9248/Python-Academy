def func(n):
	def mul():
		return n*3
	return mul

# new_func = func(7)
# print(new_func())

print(func(7)())


def func2(n):
	def mul2(m):
		return n * m
	return mul2

print(func2(7)(4))