f = open(input('FileName: '))

try:
	# data = f.readlines()
	# print(data)

	data = f.readline()
	print(data)
	
	f.seek(0) # return to the begining of the file
	
	data = f.readline()
	print(data)

except Exception as e:
	print('Error caught', e)
finally:
	f.close()
	print('Closed')