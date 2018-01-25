def pow(fn):
	def wrapper(a,b):
		return fn(a**b,b)
	return wrapper


@pow
def calc_sum(a, b):
	return a + b
print(calc_sum(2,4))
