def myFunc(*args, **kwargs):
	print(args)
	print(kwargs)
myFunc()
print('next')
myFunc(1,2,3)
print('next')
myFunc(a=1,b=2,c=3)

# positional arguments go to *args
# Keyword arguments go to **kwargs

#muFunc(x=7,10) - Error
print('Test another Function')

print('')

def Func(a,b,c,*args,**kwargs):
	print(a,b,c,args,kwargs)
Func(1,2,3)
Func(1,2,3,x=7)
Func(1,2,3,4,5,)
Func(1,2,3,4,5,x=6)
