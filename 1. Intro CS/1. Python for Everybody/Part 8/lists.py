# -*- coding: utf-8 -*-

# A list is kind of collection:
friends = ['Joseph', 'Glen', 'Sally']
carryof = ['socks', 'shirt', 'perfume']

# Lists and definite loop - best pals:
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

# Lists are mutable:
fruit = 'Banana'
# Сannot change using the index: fruit[0] = 'b'
x = fruit.lower()
print(x)

lotto = [2, 14, 26, 41, 63]
lotto[2] = 28
print(lotto)

# How long is a list:
greet = 'Hello, Bob'
print(len(greet))

x = [1, 2, 'joe', 99]
print(len(x))

# Using the range function:
for i in range(4):
    print(i)

for index in (range(len(friends))):
    friend = friends[index]
    print('Happy New Year:', friend)

# Concatenating lists using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# Lists can be sliced:
t = [9, 41, 12, 3, 74, 15]
print(t[1:3], t[:4], t[3:], t[:], sep='\n')
print('Reverse list:', t[::-1])

# Building list from scratch and using lists methods:
stuff = list()
stuff.append('book')
stuff.append(99)
stuff.append('cookie')
print(stuff)

# Is something in list?:
some = [1, 9, 21, 10, 16]
print(9 in some, ', ', 22 in some, ', ', 20 not in some, sep='')

# Lists are in order:
friends.sort()
print(friends)

# Built-in functions and lists:
nums = [3, 41, 12, 9, 74, 15]
print('len:', len(nums))
print('max:', max(nums))
print('min:', min(nums))
print('sum:', sum(nums))
print('avg:', sum(nums) / len(nums))

# Combining the use of lists and string:
abc = 'With three words'
stuff = abc.split()
for w in stuff:
    print(w)

line = 'A lot       of spaces'
etc = line.split()
print(etc)
line = 'first;second;third'
thing = line.split(';')
print(thing)