chuck_sum = 0
with open('chuck.txt', 'r') as f:
	splited_text = f.read().lower().split()
	for i in splited_text:
		if i == 'chuck':
			chuck_sum += 1
print(chuck_sum)