# filter - фильтрует элементы в массиве, стринге и тд

a = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda x: x % 2 == 0, a))
ranged_numbers = list(filter(lambda x: 4 <= x <= 7, a))

print(even_numbers)
print(ranged_numbers)