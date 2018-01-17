string = 'abracadabra'
dictMain = dict()
for i in string:
	if i in dictMain:
		dictMain[i]+=1
	else:
		dictMain[i]=1 
print(dictMain)