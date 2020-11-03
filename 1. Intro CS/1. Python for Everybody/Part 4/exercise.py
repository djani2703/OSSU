# -*- coding: utf-8 -*-

def compute_pay(hours, rate):
    print(f'In compute pay {hours} {rate}')
    if hours > 40:
        regular_pay = rate * hours
        overtime_pay = (hours - 40.0) * (rate * 0.5)
        pay = regular_pay + overtime_pay
    else:
        pay = hours * rate
    print('Returning', pay)
    return pay


string_hours = input('Enter Hours: ')
string_rate = input('Enter Rate: ')

float_hours = float(string_hours)
float_rate = float(string_rate)

human_pay = compute_pay(float_hours, float_rate)

print('Pay:', human_pay)

