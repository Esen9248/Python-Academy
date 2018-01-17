def SomeFuns(*args):
	print(args)
SomeFuns()
SomeFuns(1)
SomeFuns(1,2,3, True, -10, 'hey', {'a':'1', 'b':'2'}, ['c','d'])

def CalcSum(*args):
	res = 0
	for x in args:
		res += x
	return res
# print('Result of Sum:',CalcSum(1,2,3,4)) считает сумму значений


# считает сумму вводимых значений
numbers = input('Enter some numbers: ')
numbers = [int(n) for n in numbers.split()]
print(CalcSum(*numbers))