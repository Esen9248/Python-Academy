res = input('Do you want to procced? (Y,N) ').upper()

class ContinueCommandError(Exception):
	pass

def f():
	if res == 'Y':
		print('Yes')
	elif res == 'N':
		print('No')
	else:
		raise ContinueCommandError(res)

try:
	f()
except ContinueCommandError as e:
	print('Unknown command: ', e)