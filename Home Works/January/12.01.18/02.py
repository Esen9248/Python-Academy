def reduce_func(value, fn=None, type=None):
	res_num = 0
	res_str = ''

	if desired_type == 'number':
		for x in value:
			res_num += x
		return res_num

	if desired_type == 'string':
		for x in value:
			res_str += str(x)
		return res_str

	if desired_type == 'unit list':
		for x in value:
			res_str += str(x)
			res_list = res_str.split()
		return res_list

	if desired_type == 'cortege':
		for x in value:
			res_str += str(x)
			res_cotr = tuple(res_str)
		return res_cotr

	if desired_type == 'unit cortege':
		for x in value:
			res_str += str(x)
			res_list = res_str.split()
			res_unCort = tuple(res_list)
		return res_unCort

	if desired_type == 'dict':
		res_dict = dict()
		for x in value:
			res_dict['key-{}'.format(x)] = x
		return res_dict

desired_type = input('Enter a desired type: ')

print(reduce_func([1,2,3,4,5,6,7,'e']))