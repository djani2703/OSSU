# Using tuples:
empty_tuple = ()
print(empty_tuple)

tup_0 = (2, 'mit', 3)

print(tup_0[0])

tup_1 = (2, 'mit', 3) + (5, 6)
print(tup_0, tup_1, tup_1[1:2])

# Conveniently use to swap variable values:
x, y = 3, 10
(x, y) = (y, x)
print(x, y)

# Return more than one value from a function:
def quotient_and_ramainder(x, y):
    q = x // y
    r = x % y
    return (q, r)

(quot, rem) = quotient_and_ramainder(4, 5)

# Iterate over tuples:
def get_data(a_tuple):
    nums = ()
    words = ()
    for curr_tuple in a_tuple:
        nums = nums + (curr_tuple[0], )
        if curr_tuple[1] not in words:
            words = words + (curr_tuple[1], )
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

tswift = ((2014, 'Katy'),
          (2014, 'Harry'),
          (2012, 'Jake'),
          (2010, 'Taylor'),
          (2008, 'Joe'))

min_year, max_year, num_people = get_data(tswift)
print(f'From {min_year} to {max_year} Taylor Swift wrote songs about {num_people} people!')

# Using lists:
empty_list = []
lst_0 = [2, 'a', 4, [1, 2]]

print(len(lst_0), lst_0[0], lst_0[1:3])

# Lists is muttable:
lst_1 = [2, 1, 3]
lst_1[1] = 5

# Iterating over a list:
total = 0
lst_2 = [3, 5, 7, 2, 4]

for num in lst_2:
    total += num

# Adding elements to the list:
lst_4 = [2, 1, 3]
lst_4.append(5)

# Extend the list:
lst_5 = [4, 5, 6]
lst_4.extend(lst_5)

# Remove a specific element 5:
lst_4.remove(5)

# Remove an element at index 2:
del(lst_4[2])

# Remove the last element:
lst_4.pop()

# Convert lists to strings and back:
str_0 = 'i<3 cs'
lst_6 = list(str_0)

lst_7 = ['a', 'b', 'c']
str_1 = ''.join(lst_7)

# Sort the list:
lst_8 = [9, 6, 0, 3]

sorted(lst_8)

lst_8.sort()
lst_8.reverse()

# Cloning a list:
lst_9 = ['blue', 'green', 'grey']
lst_10 = lst_9[:]

# Mutation and iteration:
def remove_dups(lst_1, lst_2):
    lst_1_copy = lst_1[:]
    for elm in lst_1_copy:
        if elm in lst_2:
            lst_1.remove(elm)

lst_1 = [1, 2, 2, 3, 4]
lst_2 = [1, 2, 5, 6]
remove_dups(lst_1, lst_2)


def always_sunny(t1, t2):
    """ t1, t2 are non empty """
    sun = ("sunny","sun")
    print(t1, t2)
    first = t1[0] + t2[0]
    return (sun[0], first)

always_sunny(('cloudy'), ('cold',))