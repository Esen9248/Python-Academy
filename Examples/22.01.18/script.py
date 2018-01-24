fh = open('./text.txt', 'r')
data = fh.read()
fh.close() # обязательно

print(data)