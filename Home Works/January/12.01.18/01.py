array = [1,2,3,4,5,6,7,8,9,10]


def filter_func(fn, value):
	return [x for x in value if fn(x)]

print(filter_func(lambda x: x % 2 == 0, array))


