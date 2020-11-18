# -*- coding: utf-8 -*-

# Tuples are like lists:
x = ('Glen', 'Sally', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(y)
print(max(y))

for iter in y:
    print(iter)

# Things not to do with tuples:
'''
    x = (3, 2, 1)
    x.sort()
    x.append(5)
    x.reverse()
'''

# Tuples and assignment:
(x, y) = (4, 'fred')
print(x, y)
(a, _) = (99, 98)
print(a)

# Tuples and dictionaries:
d = dict()
d['csev'] = 2
d['cwen'] = 4

for key, value in d.items():
    print(key, value)

list_of_tuples = d.items()
print(list_of_tuples)

# Tuples are comparable:
res_0 = (0, 1, 2) < (5, 1, 2)
print(res_0)

res_1 = (0, 1, 2000000) < (0, 3, 4)
print(res_1)

res_2 = ('Jones', 'Sally') < ('Jones', 'Sally')
print(res_2)

res_3 = ('Jones', 'Sally') > ('Adams', 'Sam')
print(res_3)

# Sorting lists of tuples:
d = {'a': 10, 'b': 1, 'c': 22}
sort = sorted(d.items())
print(sort)

# Top 10 common words:
fhand = open('romeo.txt')

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, value in counts.items():
    newtup = (value, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for value, key in lst[:10]:
    print(value, key)

# Shorter version of code above:
c = {'a': 10, 'b': 1, 'c': 22}

sorted_lst = sorted([(v, k) for k, v in c.items()])
print(sorted_lst)