d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dic = dict()
for i in d1:
	if i in dic:
		dic[i] += d1[i]
	else:
		dic[i] = d1[i]
for i in d2:
	if i in dic:
		dic[i] += d2[i]
	else:
		dic[i] = d2[i]
print(dic)