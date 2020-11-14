# -*- coding: utf-8 -*-

# Using open:
fhandle = open(file='mbox.txt', mode='r')
print(fhandle)

# File handle as a sequence:
xfile = open('mbox.txt')

for line in xfile:
    print(line)

# Counting lines in a file:
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count += 1
print('Line count:', count)

# Reading the 'whole' file:
fhand = open('mbox.txt')
inp = fhand.read()
print(inp[:20])

# Searching through a file:
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('By'):
        print(line)

# Skipping with continue:
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('By'):
        continue
    print(line)

# Using in to select lines:
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

# Prompt for file name:
fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)

count = 0
for line in fhand:
    if line.startswith('at'):
        count += 1
print('There were', count, 'at lines in', fname, 'file.')