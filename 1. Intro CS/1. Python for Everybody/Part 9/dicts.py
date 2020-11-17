# -*- coding: utf-8 -*-

# Dictionaries:
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print(purse)
print(purse['candy'])

purse['candy'] += 2
print(purse)

# Dictionary literals:
jjj = {'chuck': 1, 'freed': 42, 'jan': 100}
print(jjj)
ooo = {}
print(ooo)

# Many counters with a dictionary:
ccc = dict()
ccc['csev'] = 1
ccc['sven'] = 1
print(ccc)
ccc['sven'] += 1
print(ccc)

# Count names using dictionary:
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

# The get method for dictionaries:
name = 'csev'
if name in counts:
    val0 = counts[name]
else:
    val0 = 0

val1 = counts.get(name, 0)
print(val0, val1)

# Simplified counting with get()
counts = dict()
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# Counting pattern:
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()
print('Words:', words)

print('Counting:')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)

# Define loops and dictionaries:
counts = {'chuck': 1, 'freed': 42, 'jan': 100}
for key in counts: 
    print(key, counts[key])

# Two iteration variables:
for key, value in counts.items():
    print(key, value)