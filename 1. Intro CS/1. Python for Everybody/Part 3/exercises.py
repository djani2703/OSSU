# -*- coding: utf-8 -*-

# Exercises: 3.1, 3.2
str_hours = input('Enter hours: ')
str_rate = input('Enter rate: ')
try:
    float_hours = float(str_hours)
    float_rate = float(str_rate)
except:
    print('Error, please enter correct numeric input..')
    exit()

if float_hours > 40:  
    regular_pay = float_hours * float_rate
    overtime_pay = (float_hours - 40.0) * (float_rate * 0.5)
    human_pay = regular_pay + overtime_pay
else:
    human_pay = float_hours * float_rate

print('Pay:', human_pay)