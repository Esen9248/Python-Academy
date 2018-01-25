def pow(fn):
	def wrapper(phone):		
		if phone[0:3] == '996' and len(phone) == 12:
			return phone
		else:
			print('Not a phone number')
	return wrapper

@pow
def print_phone_number(phone): return phone

enter_phone = input('Enter a phone number: ')
print(print_phone_number(enter_phone))