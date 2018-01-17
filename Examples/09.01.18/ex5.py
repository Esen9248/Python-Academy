def func(a=None, b=None):
	print(a,b)
func()
func(45)
func(45,10)
func(a=45, b=10)
func(b=9)
func(b=6,a=7)


#positional args first (args with NO default value)

def someFunc(a,b,c=10,d=False):
	print(a,b,c,d)
someFunc(1,4)
someFunc(1,4,5)