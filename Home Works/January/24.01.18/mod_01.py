from math import sqrt
Pi = 3.14

def square_area(a):
	return 'S(square)=', a**2

def circle_area(r):
	return 'S(circle)=', Pi*(r**2)

def triangle_area(a,h):
	return 'S(triangle)=', (a/2)*h

def quadratic_equation(a,b,c):
	d = (b**2)-(4*a*c)
	if d < 0:
		return 'Error'
	elif d == 0:
		x = -b/(2*a)
		return 'x=', x
	else:
		x1 = (-b + sqrt(d)) / (2*a)	
		x2 = (-b - sqrt(d)) / (2*a)	
		return 'x1=', x1, 'x2=', x2

def cube_of_sum(a,b):
	# (a+b)^3 =  a^3 + 3a^2b + 3ab^2 + b^3
	return '(a+b)^3=', a**3 + (3*(a**2)*b) + (3*a*(b**2)) + b**3