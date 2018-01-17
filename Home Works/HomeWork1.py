# First task
for i in range(1500, 2700):
	if (i%7==0) and (i%5==0):
		print (i)


# Second task
a = 0
while a<5:
	print("*"*a)
	a+=1
	if a==5:
		while a>0:
			print("*"*a)
			a-=1
			if a==0:
				break
		break