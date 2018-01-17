# -*- encoding: utf-8 -*-

print('Hello World')
print(u"Привет всем") # кириллица Python2

d = {
	'a': 1,
	'b': 2,
	'c': 3,
}
print(d.get('a'))
print(d.get('d'))
print(d.get('d', 0))