from functools import reduce

objects = [
	{'year': 1999, 'item': 'a'},
	{'year': 1999, 'item': 'h'},
	{'year': 2000, 'item': 'b'},
	{'year': 2001, 'item': 'c'},
	{'year': 2002, 'item': 'd'},
]
print(objects)

print(list(map(lambda x: x ['item'], list(filter(lambda x: x['year'] == 1999, objects)))))



def calc(acc,o):
	year = o['year']
	if year not in acc:
		acc[year] = []
	acc[year].append(o['item'])
	return acc

print(reduce(calc, objects, {})[1999])