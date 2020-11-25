# -*- coding: utf-8 -*-

import re

# Exercise 1:
pattern = input('Enter a regular expression: ', )
fname = 'mbox-short.txt'
fhand = open(fname)

count = 0
for line in fhand:
    line = line.rstrip()
    matches = re.findall(pattern, line)
    if len(matches) > 0:
        count += 1
print(f'{fname} had {count} lines than matched {pattern}')

# Exercise 2:
fname = input('Enter file: ')
fhand = open(fname)

nums = []
for line in fhand:
    curr_nums = re.findall('[0-9]+', line)
    if curr_nums:
        nums.extend(curr_nums)

nums = [int(num) for num in nums if int(num) > 0]
avg = int(sum(nums) / len(nums))
print('Average: ', avg)