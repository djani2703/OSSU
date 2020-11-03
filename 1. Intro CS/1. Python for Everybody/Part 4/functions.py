# -*- coding: utf-8 -*-

x = 5
print('Hello')

# Creating an our remembering and reusable bit of code:
def pring_lyrics():
    print('I\'m a lumberjack, and I\'m okay.')
    print('I sleep all night and i work all day.')

print('Yo')
pring_lyrics()

x = x + 2
print(x)

# Parameters of the function:
def greet_1(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet_1('fr')

# Return values of the function:
def greet_2():
    return 'Hello'

print(greet_2(), 'Glenn')
print(greet_2(), 'Sally')

# Multiple Parameters / Arguments of function:
def add_two(a, b):
    added = a + b
    return added

x = add_two(3, 5)
print(x)