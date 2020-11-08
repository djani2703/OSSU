# -*- coding: utf-8 -*-

# String date type:
str1 = 'Hello, '
str2 = 'there!'
bob = str1 + str2
print(bob)

str3 = '123'
x = int(str3) + 1
print(x)

# Reading and converting:
name = input('Enter: ')
print(name)
apple = input('Enter: ')
x = int(apple) - 10
print(x)

# Looking inside strings:
fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x-1]
print(w)

# Looping through strings:
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

for letter in fruit:
    print(letter)

# Looping and counting:
word = 'banana'
count = 0
for letter in word:
    if  letter == 'a':
        count += 1
print(count)

# Slicing strings:
str4 = 'Monty Python'
print(str4[0:4])
print(str4[6:7])
print(str4[6:20])

# String concatenation:
a = 'Hello'
b = a + ' ' + 'There'
print(b)

# Using in as a logical operator:
fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
if 'a' in fruit:
    print('Found it!')

# String comparison:
if word == 'banana':
    print('All right, bananas.')
elif word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('Other all right, bananas.')

# String library:
greet = 'Hello, Bob'

# find(substr):
pos0 = greet.find('ob')
print(pos0)
pos1 = greet.find('NN')
print(pos1)

# upper():
upp_greet = greet.upper()
print(upp_greet)

# lower()
low_greet = greet.lower()
print(low_greet)

# replace(old, new):
new_greet = greet.replace('Bob', 'Jane')
print(new_greet)

# lstrip(), rstrip(), strip():
greet = '    Hello, Bob    '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

# startswith('something')
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

# Parsing and extracting:
data = 'Form stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)