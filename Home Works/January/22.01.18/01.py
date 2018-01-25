my_dict = dict()
chuck_len = None
with open('chuck.txt', 'r') as f:
	my_read = f.read()
	chuck_len = str(len(my_read))
	for i in my_read:
		if i in my_dict:
			my_dict[i]+=1
		else:
			my_dict[i]=1 
with open('abc.txt', 'a') as new_chuck:
	new_chuck.writelines(str(my_dict))
	new_chuck.writelines('\n')
	new_chuck.writelines(chuck_len)