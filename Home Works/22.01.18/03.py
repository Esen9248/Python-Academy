ChuckSum = 0
with open('chuck.txt', 'r') as f:
	SplitedText = f.read().split()
	for i in SplitedText:
		if i == 'Chuck':
			ChuckSum += 1
print(ChuckSum)