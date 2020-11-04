# -*- coding: utf-8 -*-

# Repeated steps(1):
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
print('n = ', n, sep='')

# Another loop:
n = 0
while n > 0:
    print('Lather')
    print('Rinse')
print('Dry off!')

# Breaking out of a loop:
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# Finishing an iteration with continue:
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    elif line == 'done':
        break
    print(line)
print('Done!')

# Simple definite loop:
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

# A definite loop with strings:
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print(f'Happy New Year: {friend}!')
print('Done!')

# Finding the largest value:
largest_so_far = -1
print(f'Before: {largest_so_far}')
for current_number in [9, 41, 12, 3, 74, 15]:
    if current_number > largest_so_far:
        largest_so_far = current_number
    print(largest_so_far, current_number)
print(f'After: {largest_so_far}')

# Counting in a loop:
zork = 0
print(f'Before: {zork}')
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print(f'After {zork}')

# Summing in a loop:
sum = 0
print(f'Before: {sum}')
for thing in [9, 41, 12, 3, 74, 15]:
    sum = sum + thing
    print(sum, thing)
print(f'After: {sum}')

# Finding the average in a loop:
count, sum = 0, 0
print(f'Before: count - {count}, sum - {sum}')
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(f'{count}, {sum}, {value}')
print(f'After: count - {count}, sum - {sum}, avg - {sum/count}')

# Filtering in a loop:
print('Before:')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large number: ', value, sep='')
print('After:')

# Search using a boolean variable:
found = False
print('Before:', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After:', found)

# Finding the smallest value:
smallest = None
print('Before:', smallest)
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After:', smallest)