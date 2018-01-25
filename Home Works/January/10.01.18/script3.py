string = input('Enter some text: ')
def Func():
	if string == string[::-1]:
		res = 'True'
	else:
		res = 'False'
	return res
print(Func())