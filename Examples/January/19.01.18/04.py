try:
	print('res', 10 / 0)
except ZeroDivisionError:
	print('Can\'t divide')
else: # will execute only if no Exception was raised
	print('No exceptions were raised')
finally: # will execute regardless Exception was raised or not
	print('This text will show up always')

print('Exit')