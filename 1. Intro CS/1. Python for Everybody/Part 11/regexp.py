# -*- coding: utf-8 -*-

# Using re.search() like find()

# String version (find):
fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# RegExp version (search):
import re

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# Matching and extracting data:
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
y = re.findall('[AEIOU]+', x)
print(y)

# Warning: Greedy matching:
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

# Fine-tuning string extraction:
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('^From (\S+@\S+)', x)
print(y)

# String parsing example:
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
sppos = data.find(' ', atpos)
host = data[atpos+1:sppos]
print(host)

# The double split pattern version:
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# The Regex version:
y = re.findall('^From .*@([^ ]*)', data)
print(y)

# Spam confidence:
fhand = open('mbox-short.txt')
numlist = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

# Escape character:
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)