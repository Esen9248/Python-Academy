class A(object):
	def __init__(self):
		self.public_attr = 1111
		self.__private_attr = 2222 
		self._protected_attr = 3333

	def print_public_attr(self):
		print(self.public_attr)

	def print_private_attr(self):
		print(self.__private_attr)

	def call_private(self): # method to call private method
		self.__private_method()

	def __private_method(self):
		print('private method(function)')

class B(A):
	def print_protected_attr(self):
		print(self._protected_attr)