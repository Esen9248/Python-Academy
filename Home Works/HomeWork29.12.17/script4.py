first = list()
second = list()
CompleteList = list()
dic = {'1':['a','b'], '2':['c','d']}
first = dic['1']
second = dic['2']
for i in first:
	for x in second:
		CompleteList.append(i+x)
for i in CompleteList:
	print(i)
