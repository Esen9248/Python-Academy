#  filter, map, reduce

a = [1,2,3,4,5,6,7,8,9,10]

def filter_func(x):
	return x % 2 == 0

even_numbers = list(filter(filter_func, a))

print(even_numbers)


def filter_func2(x):
	return 4 <= x <= 7

ranged_numbers = list(filter(filter_func2, a))

print(ranged_numbers)