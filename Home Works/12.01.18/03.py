def transform(x,y):
	x['key-{}'.format(y)] = y
	return x


def reduce_func(value, fn, res_type = None):
	if res_type == None:
		res_type = value[0]
	for x in value:
		res_type = fn(res_type, x)
	return res_type

print(reduce_func([1,2,3], transform, dict()))


def reduce_func2(value, fn, res_type = None):
	if res_type == None:
		res_type = value[0]
	for x in value:
		res_type = fn(res_type, x)
	return res_type

print(reduce_func2([1,2,3], lambda x, y: x + y))

