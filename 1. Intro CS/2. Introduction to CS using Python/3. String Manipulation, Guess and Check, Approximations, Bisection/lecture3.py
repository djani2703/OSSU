# Can get the length of a string using len ():
str_1 = 'abc'
print(len(str_1))

#  Can slice string using [start:stop:step]:
str_2 = 'abcdefgh'
print(str_2[3:6], str_2[3:6:2], end=' ')
print(str_2[::], str_2[::-1], end=' ')
print(str_2[4:1:-2])

# Strings are immutable:
str_3 = 'hello'
str_3 = 'y' + str_3[1:len(str_3)]
print(str_3)

# Strings and loops:
str_4 = 'abcdefgh'

for index in range(len(str_4)):
    if str_4[index] in ['i', 'u']:
        print('There is an i or u..')

for char in str_4:
    if char in ['i', 'u']:
        print('There is an i of u..')

# Creating Robot Cheerleaders:
an_letters = 'aefhilmnorsxAEFHILMNORSX'

word = input('I will cheer for you! Enter a word: ')
times = int(input('Enthusiasm level (1-10): '))

for char in word:
    if char in an_letters:
        print('Give me an ' + char + '! ' + char)
    else:
        print('Give me a ' + char + '! ' + char)

print('What does that spell?')

for i in range(times):
    print(word, '!!!')

# Guess and check algorithm:
cube = 8
guess = 0

for guess in range(abs(cube) + 1):
    if guess ** 3 >= abs(cube):
        break

if guess ** 3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess *= -1
    print('Cube root of ' + str(cube) + ' is ' + str(guess))

# Approximate solution algorithm:
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess ** 3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1

print('num_guesses =', num_guesses)

if abs(guess ** 3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)

# Bisection search:
cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube

guess = (low + high) / 2.0
while abs(guess ** 3 - cube) >= epsilon:
    if guess ** 3 < cube:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0
    num_guesses += 1

print('num guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)