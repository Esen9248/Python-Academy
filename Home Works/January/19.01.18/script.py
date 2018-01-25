def num():
	number = int(input('Enter a number: '))
	return number

# def op():
# 	operator = int(input('Enter an operator: '))
# 	return operator

cont = input ('Do you want to continue? (Y,N) ')
res = 0

while cont.upper() == 'Y':
	num()
	if operator == '+':
		res += num
print(res)