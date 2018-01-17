a = list()
for i in range(10):
	a.append(i)
print(a)

# list comprehantion
b = [x for x in range(10)]
print(b)


c = [(x+4*5) for x in range(10)]
print(c)


d = ['{:.2f}'.format(x * 3 / 7) for x in range(10)]
print(d)

e = [x for x in range(20) if x % 2 ==0]
print(e)