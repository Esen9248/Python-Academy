from ex_mod import A, B
if __name__ == '__main__':
	a = A()
	b = B()
	print('public', a.public_attr)
	a.print_private_attr()
	a.print_public_attr()
	a.call_private()
	b.print_protected_attr()
	# a.__private_method() - 'A' object has no attribute '__private_method'
	# print('private', a.__private_attr) #- 'A' object has no attribute '__private_attr'
	