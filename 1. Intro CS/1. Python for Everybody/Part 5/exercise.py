# -*- coding: utf-8 -*-

count = 0
total = 0.0

while True:
    string_value = input('Enter a number: ')
    if string_value == 'done': 
        break
    try:
        flat_value = float(string_value)
    except:
        print('Invalid input')
        continue
    count += 1
    total += flat_value

print(total, count, total/count)