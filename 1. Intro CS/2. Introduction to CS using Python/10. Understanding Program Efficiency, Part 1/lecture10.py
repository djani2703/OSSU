# Timing a program:
import time

def performance_time(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        print(f'Time of function {func.__name__} execution: {end_time - start_time} sec')
        print(f'Result: {result}')
        return result
    return wrapper

@performance_time
def celcium_to_fahr(celcium):
    return celcium * 9/5 + 32

@performance_time
def my_sum(x):
    total = 0
    for i in range(1,x+1,1):
        total += i
    return total

# Search for an element in list algorithm:
def search_for_elm(elm_list, elm):
    for curr_elm in elm_list:
        if curr_elm == elm:
            return True
    return False

# Liniar search on unsorted list:
def linear_search(elm_list, elm):
    found = False
    for index in range(len(elm_list)):
        if elm_list[index] == elm:
            found = True
    return found

# Linear search on sorted list:
def linear_sorted_search(elm_list, elm):
    for i in range(len(elm_list)):
        if elm_list[i] == elm:
            return True
        if elm_list[i] > elm:
            return False
    return False

# Quadratic complexity - Subset:
def is_subset(list_1, list_2):
    for elm_1 in list_1:
        matched = False
        for elm_2 in list_2:
            if elm_1 == elm_2:
                matched = True
                break
            if not matched:
                return False
    return True

# Quadratic complexity - Intersect:
def intersect(list_1, list_2):
    tmp_list = []
    for elm_1 in list_1:
        for elm_2 in list_2:
            if elm_1 == elm_2:
                tmp_list.append(elm_1)
    result = []

    for elm in tmp_list:
        if elm not in result:
            result.append(elm)
    return result


if __name__ == '__main__':
    celcium_to_fahr(100000)
    my_sum(1000000)
    search_for_elm([13, 27, 51, 34, 44, 1, 72], 72)
    linear_search([13, 27, 51, 34, 44, 1, 72], 72)
    linear_sorted_search([13, 27, 51, 55, 74, 102, 172], 72)
    is_subset([13, 27, 51, 34, 44, 1, 72], [13, 27, 51, 55, 74, 102, 172])
    intersect([13, 27, 51, 34, 44, 1, 72], [13, 27, 51, 55, 74, 102, 172])