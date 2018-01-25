def calc_word(word):
	res = {}
	for w in word:
		if w not in res:
			res[w] = 0
		res[w] += 1
	return res

result = calc_word(input('Enter a word: '))
print(result)


def Multiply(a,b):
	print('a is {a}, b is {b}'.format(a=a,b=b))
Multiply(1,2)