# -*- coding: utf-8 -*-

fhand = open('mbox-short.txt')
for line in fhand:
    strip_line = line.rstrip()
    upper_line = strip_line.upper()
    print(upper_line)