# Lists
a = [0,1,2,3,4,5]
empy_list = []
b = [
	[0,1,2,3],
	[4,5,6],
]
print('a', a)
print('first a element:', a[1])
print('empty list', empy_list)
print('b', b)
print()

print('length for list "a" is:', len(a))
# lists how to iterate

for i in a:
	print(i)


res = 0
for i in a:
	res = res + i
print('res: {}'.format(res))