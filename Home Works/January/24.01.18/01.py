from mod_01 import (
	square_area,
	circle_area, 
	triangle_area,
	square_equation,
	cube_addition,
)

if __name__ == '__main__':
	print(square_area(4))
	print(circle_area(3))
	print(triangle_area(6,5))
	print(square_equation(2,4,2)) # 2x^2 + 4x + 2 = 0
	print(cube_addition(3,4))