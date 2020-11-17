# -*- coding: utf-8 -*-

fname = input('Enter file: ')

if len(fname) < 1:
    fname = 'clown.txt'

fhand = open(fname)

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

largest = -1
the_word = None
for key, value in counts.items():
    if value > largest:
        largest = value
        the_word = key

print(the_word, largest)