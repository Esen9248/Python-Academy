# map - изменяет элементы в массиве. стринге и тд

a = [1,2,3,4,5,6,7,8,9,10]

new_list = list(map(lambda x: x** 2, a))

print(list(map(lambda x: x**2, a)))
print(new_list)

string = 'Hello Meeen'

print(''.join(list(map(lambda x: x*2, string))))