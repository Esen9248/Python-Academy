def Calc(*args, op):
	if op == '+':
		res = 0
		for x in args:
			res += x

	if op == '*':
		res = 1
		for x in args:
			res *= x

	if op == '-':
		for x in range(0,len(args)):
			res = args[x-1] - args[x]

	if op == '/':
		for x in range(0,len(args)):
			res = args[x-1] / args[x]
	return res

numbers = [int(n) for n in input('Enter two numbers: ').split()]

operator = input('Enter an operator: ')


print(Calc(*numbers, op=operator))