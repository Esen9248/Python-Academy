filename = input('Enter new filename: ')

f = open(filename, 'w')

try:
	f.write('test file write\n')

except Exception as e:
	print('Error caught', e)
finally:
	f.close()
	print('Closed')	