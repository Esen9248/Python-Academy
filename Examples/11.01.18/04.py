# reduce - приравнивает массив, стринг и тд к одному значению

from functools import reduce

a = [1,2,3,4,5,6,7,8,9,10]

reduced_value = reduce(lambda x, y: x * y, a)

print(reduced_value)

print(reduce(lambda x,y: x*y, [1,2,3]))


def transform(x,y):
	x['key-{}'.format(y)] = y
	return x

returned_map = reduce(transform, [1,2,3], {})
print(returned_map)


print(reduce(lambda x, y: x + str(y), [1,2,3], ''))