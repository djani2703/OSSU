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

tmp = list()
for k, v in counts.items():
    new_tuple = (v, k)
    tmp.append(new_tuple)

tmp = sorted(tmp, reverse=True)
for v, k in tmp[:5]:
    print(k, v)