number = int(input('Enter a number: '))
interval = int(input('Enter start of interval: '))
interval2 = int(input('Enter end of interval: '))

def Func():
	if number in range(interval, interval2+1):
		res = 'True'
	else:
		res = 'False'
	return res
	
print(Func())