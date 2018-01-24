myDict = dict()
with open('chuck.txt', 'r') as f:
	for i in f.read():
		if i in myDict:
			myDict[i]+=1
		else:
			myDict[i]=1 
print(myDict)