def pow(fn):
	def wrapper(x,y):
		if y == 0:
			print('Error')
		else: 
			return x / y
	return wrapper 

@pow
def div(x, y): return x / y
print(div(4,0))