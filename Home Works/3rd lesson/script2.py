a = [60,-2,3,4,5,32,4,6]
print(a)
b = a[1]
c = a[1]
for i in a:
	if b >= i:
		b = i
	if c <= i:
		c = i
print('max:', c)
print('min:', b)