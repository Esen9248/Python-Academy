from mymodule import my_pow, Pi
from mydir.othermodule import my_sum
x, y = [int(x) for x in input('Enter two numbers: ').split()]

print('sum of {} and {} = {}'.format(x, y, my_sum(x,y)))

print('{} ^ {} = {}'.format(x, y, my_pow(x,y)))

print('Pi = ', Pi)