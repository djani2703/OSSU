# Letters, special characters, spaces, digits:
hi = 'hello there'

# Concatenate strings:
name = 'ana'

greet = hi + name
print(greet)

greeting = hi + ' ' + name
print(greeting)

silly = hi + (' ' + name) * 3
print(silly)

# Input/Output - print():
x = 1
x_str = str(x)

print('my favorite num is', x, '.', 'x =', x)
print('my favorite num is ' + x_str + '. ' + 'x = ' + x_str)

# Input/Output - input(''):
text = input('Type anything... ')
print(5 * text)

num = int(input('Type a number... '))
print(5 * num)

# Indentation:
x = float(input('Enter a number for x: '))
y = float(input('Enter a number for y: '))

if x == y:
    print('x and y are equal')
    if y != 0:
        print('Therefore, x / y is:', x / y)
elif x < y:
    print('x is smaller')
else:
    print('y is smaller')

# while loop example:
way = input('You\'re in the Lost Forest. Go left or right? ')

while way == 'right':
    way = input('You\'re in the Lost Forest. Go left or right? ')

print('You got out of the Lost Forest!\n\o/')

# Control flow - while and for loops:
n = 0
while n < 5:
    print(n)
    n = n + 1

for n in range(5):
    print(n)

# Using range(start, stop, step):
my_sum = 0
for i in range(5, 11, 2):
    my_sum += i
print(my_sum)

# Using break statement:
my_sum
for i in range(5, 11, 2):
    my_sum += i
    if my_sum == 5:
        break
        my_sum += 1
print(my_sum)

# Perfect squares:
ans = 0
neg_flag = False
x = int(input('Enter an integer: '))

if  x < 0:
    neg_flag = True

while ans ** 2 < x:
    ans = ans + 1

if ans ** 2 == x:
    print('Square root of', x, 'is', ans)
else:
    print(x, 'is not a perfect square')
    if neg_flag:
        print('Just checking.. Did you mean', -x, '?')