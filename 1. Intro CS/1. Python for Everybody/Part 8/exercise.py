# -*- coding: utf-8 -*-

fhandler = open('mbox-short.txt')

for line in fhandler:
    line = line.rstrip()
    words = line.split()
    if words[0] != 'From' or len(words) < 3:
        continue
    print(words[2])