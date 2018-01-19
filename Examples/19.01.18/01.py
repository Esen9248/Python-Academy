x, y = [int(i) for i in input('Enter two numbers: ').split()]

res = None
try:
	res = x/y
except:
	print('Can`t divide {} by {}'.format(x,y))
print(res)