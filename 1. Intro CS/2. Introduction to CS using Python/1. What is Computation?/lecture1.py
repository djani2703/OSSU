from random import randint

# Looking for a Google Cardboard winner:
win_number = randint(16, 272)
print(f'Won the number {win_number}!')

# Looking for area of circle:
pi = 3.14159
radius = 2.2
area = pi * (radius ** 2)

# Rebind variable radius:
radius = radius + 1

# Print the value of variables out:
print(f'Area is equal {area}')
print(f'Radius is equal {radius}')

# Bad variable name. Don't use names like that:
a_very_long_variable_name_dont_name_them_this_long_pls = 0

# PSET 0:
from math import log
x = input('Enter number x: ')
y = input('Enter number y: ')

try:
    x = int(x)
    y = int(y) 
except:
    x, y = 1, 1 

print('x**y =', x**y)
print('log(x) = ', log(x, 2), sep='')