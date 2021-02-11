# Glass box testing:
def my_abs(x):
    '''Assumes x is an int. Returns x if x >= 0 and -x otherwise'''
    return -x if x < 0 else x

# Dealing with exceptions:
try:
    a = int(input('Tell me one number: '))
    b = int(input('Tell me another number: '))
    print('a / b =', a / b) 
except:
    print('Bug in user input.')

# Handling specific exceptions:
try:
    a = int(input('Tell me one number: '))
    b = int(input('Tell me another number: '))
    print('a / b = ', a / b)
    print('a + b = ', a + b)
except ValueError:
    print('Could not convert to a number.')
except ZeroDivisionError:
    print('Can\'t divide by zero')
except:
    print('Something went very wrong.')

# Example: Raising an Exception:
def get_ratios(l1, l2):
    '''Assumes: l1 and l2 are lists of equal length of numbers
       Returns: a list containing l1[i]/l2[i]'''
    ratios = []
    for index in range(len(l1)):
        try:
            ratios.append(l1[index]/l2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

# Exceptions and lists:
def avg_0(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print('warning: no grades data')
        return 0.0

def avg_1(grades):
    assert not len(grades) == 0, ' no grades data'
    return sum(grades) / len(grades)

def get_stats(class_list):
    new_stats = []
    for person in class_list:
        new_stats.append([person[0], person[1], avg_1(person[1])])
    return new_stats


if __name__ == '__main__':
    test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
                [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
                [['captain', 'america'], [80.0, 70.0, 96.0]],
                [['deadpool'], []]]

    get_stats(test_grades)