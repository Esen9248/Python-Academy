# Strip() - Удаление пробельных символов в начале и в конце строки,
# lower() - переводит в нижний регистр

def div(x,y):
	return x / y

while input('Do you want to continue? (Y/N) ').strip().lower() == 'y':
	try:
		x, y = [int(i) for i in input('Enter two numbers: ').split()]
		print('result', div(x,y))
	except ZeroDivisionError as e:
		try:
			res = 'sff' / 8
		except TypeError:
			print('TypeError has happend')
		print('Zero Division Error:', e)
	except ValueError as e:
		print('Value Error', e)
