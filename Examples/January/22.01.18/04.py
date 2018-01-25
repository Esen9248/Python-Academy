filename = input('Enter new filename: ')

f = open(filename, 'w')
strings = [
'Hey',
'Men',
'Aye\n',
'Hello\n',
]

try:
	for i in strings:
		f.write(i)
except Exception as e:
	print('Error caught', e)
finally:
	f.close()
	print('Closed')	