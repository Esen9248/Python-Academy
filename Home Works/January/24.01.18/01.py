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
	print(square_equation(3,8,4)) # 3x^2 + 8x + 4 = 0
	print(cube_addition(3,4))