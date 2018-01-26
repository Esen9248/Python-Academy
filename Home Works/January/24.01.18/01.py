from mod_01 import (
	square_area,
	circle_area, 
	triangle_area,
	quadratic_equation,
	cube_of_sum,
)

x_sq = int(input('Enter lengh of square side: '))
x_cr = int(input('Enter circle radius: '))
a_tr, h_tr = [int(i) for i in input('Enter lengh of triangle side and height: ').split()]
a_qe, b_qe, c_qe = [int(i) for i in input('Enter a, b, c in ax^2+bx+c=0 addicion: ').split()]
x_cs, y_cs = [int(i) for i in input('Enter a, b in (a+b)^3 addition: ').split()]

if __name__ == '__main__':
	print(square_area(x_sq))
	print(circle_area(x_cr))
	print(triangle_area(a_tr, h_tr))
	print(quadratic_equation(a_qe,b_qe,c_qe)) # 2x^2 + 4x + 2 = 0
	print(cube_of_sum(x_cs,y_cs))