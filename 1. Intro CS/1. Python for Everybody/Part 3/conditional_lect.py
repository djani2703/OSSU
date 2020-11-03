# -*- coding: utf-8 -*-

# Conditional steps(1):
x = 5

if x < 10:
    print(f'{x} smaller than 10')
if x > 20:
    print(f'{x} bigger than 20')

print('Finish!')

# Conditional step(2):
if x == 5: 
    print('Equals 5')
if x > 4:
    print('Greater than 4')
if x < 6:
    print('Less than 6')
if x <= 5:
    print('Less than or Equals 5')
if x != 6:
    print('Not equal 6')

# Conditional step(3):
x = 42
if x > 1:
    print(f'{x} more than 1')
    if x < 100:
        print(f'{x} less than 100')
print('All done!')

# More conditional structures...
x = 5
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done!')

# The try / except Structure
# Try/except example (1):
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First:', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second:', istr)

# Try/except example (2):
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work!')
else:
    print('Not a number')
