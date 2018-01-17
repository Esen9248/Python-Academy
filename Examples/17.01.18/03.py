def pow(fn):
	def wrapper(a,b):
		return fn(a**b,b)
	return wrapper

# print(pow(calc_sum)(2,4))


@pow
def calc_sum(a, b):
	return a + b
print(calc_sum(2,4))
