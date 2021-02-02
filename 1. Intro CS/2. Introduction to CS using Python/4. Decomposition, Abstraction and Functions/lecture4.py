# How to write and call/invoke a function:
def is_even(i):
    '''
    Input: i, a positive int
    Returns True if i is even, otherwise False
    '''
    return i % 2 == 0

# Variabe scope:
def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x

# Difference between function with and without return:
def is_even_with_return(i):
    '''
    Input i, a positive int
    Returns True if i is even, otherwise False
    '''
    print('With return: ', end='')
    remainder = i % 2
    return remainder == 0

def is_even_without_return(i):
    '''
    Input i, a positive int
    Doesn't return anything
    '''
    print('Without return: ', end='')
    _ = i % 2

# Functions as arguments:
def func_a():
    print('Inside func_a')

def func_b(y):
    print('Inside func_b')
    return y

def func_c(z):
    print('Inside func_c')
    return z()

# Scope exampes:
def scope_ex_1(y):
    x = 1
    x += 1
    print(x)

def scope_ex_2(y):
    print(x)
    print(x + 1)

def scope_ex_3(y):
    # x += 1 - do not change the global variables
    pass

# Scope details:
def g(x):
    def h():
        _ = 'abc'
    x = x + 1
    print('g: x =', x)
    h()
    return x


if __name__ == '__main__':
    # How to write and call/invoke a function:
    is_even(3)

    # Variabe scope:
    x = 3
    z = f(x)

    # Difference between function with and without return:
    print(is_even_with_return(3))
    print(is_even_without_return(3))

    # Use the is_even function later on in the code:
    print('All numbers between 0 and 20: even or not')
    for i in range(20):
        if is_even(i):
            print(i, 'even')
        else:
            print(i, 'odd')

    # Functions as arguments:
    print(func_a)
    print(5 + func_b(2))
    print(func_c(func_a))

    # Scope exampes:
    x = 5
    scope_ex_1(x)
    print(x)

    scope_ex_2(x)
    print(x)

    scope_ex_3(x)
    print(x)

    # Scope details:
    x = 3
    z = g(x)
    print(z)