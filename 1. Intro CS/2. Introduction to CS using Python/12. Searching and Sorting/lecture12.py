import random
# Inner functions and decorators:
def show_result(func):
    def wrapper(*args):
        print(f'Result: {func(*args)}')
    return wrapper

def is_sorted(list):
    for index in range(len(list)-1):
        if list[index] > list[index+1]:
            return False
    return True

# Linear search on unsorted list:
@show_result
def linear_search_unsorted(list, elm):
    found = False
    for curr_elm in list:
        if curr_elm == elm:
            found = True
    return found

# Linear search on sorted list:
@show_result
def linear_search_sorted(list, elm):
    if list[0] > elm:
        return False
    for index in range(len(list)):
        if list[index] == elm:
            return True
    return False

# Complexity of Bogo sort:
@show_result
def bogo_sort(list):
    while not is_sorted(list):
        random.shuffle(list)
    return list

# Complexity of Bubble sort:
@show_result
def bubble_sort(list):
    for _ in range(len(list)-1):
        for j in range(0, len(list)-1, 1):
            if list[j] > list[j+1]:
                (list[j], list[j+1]) = (list[j+1], list[j])
    return list    

# Complexity of Selection sort:
@show_result
def selection_sort(list):
    suffix_st = 0
    while suffix_st != len(list):
        for index in range(suffix_st, len(list)):
            if list[index] < list[suffix_st]:
                list[suffix_st], list[index] = list[index], list[suffix_st]
        suffix_st += 1
    return list                

# Complexity of Merge sort:
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(list):
    if len(list) < 2:
        return list[:]
    else:
        middle = len(list)//2
        left = merge_sort(list[:middle])
        right = merge_sort(list[middle:])
        return merge(left, right)
        

if __name__ == '__main__':
    # Searching algorithms:
    linear_search_unsorted([3, 42, 15, 2, 52, 24, 82], 2)
    linear_search_sorted([3, 15, 17, 21, 34, 45, 52], 17)

    # Sorting algorithms:
    bogo_sort([3, 5, 1, 2, 6])
    bubble_sort([3, 5, 1, 2, 6])
    selection_sort([3])
    merge_sort([1, 4, 5, 2, 8, 12])