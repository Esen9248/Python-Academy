d = {}
d1 = dict() 
d['a'] = 'some string'
d['b'] = 100
d['c'] = [1,2,3,4,5]
d['d'] = [1,2,3, 'some text', True, {'k': 'Vocabulary index'}]

print(d['a'])
print(d['b'])
print(d['c'])
print(d['d'])

for i in d['c']:
	print(i)