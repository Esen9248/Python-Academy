def div(x,y):
	return x / y

while input('Do you want to continue? (Y/N) ').strip().lower() == 'y':
	try:
		x, y = [int(i) for i in input('Enter two numbers: ').split()]
		print('result', div(x,y))
	except:
		print('Error: Cant\'t divide')

