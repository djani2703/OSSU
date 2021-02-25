# Bisection search implementation 1:
def bisect_search(list, elm):
    if len(list) == 0:
        return False
    else:
        half = len(list) // 2
        if elm == list[half]:
            return True
        elif elm > list[half]:
            return bisect_search(list[half+1:], elm)
        else:
            return bisect_search(list[:half], elm)

# Bisection search implementation 2:
def bisect_search_2(list, elm):
    def bisect_search_helper(list, elm, low, high):
        if high == low:
            return list[low] == elm
        mid = (low + high) // 2
        if list[mid] == elm:
            return True
        elif list[mid] > elm:
            if low == mid:
                return False
            else:
                return bisect_search_helper(list, elm, low, mid - 1)
        else:
            return bisect_search_helper(list, elm, mid + 1, high)
    if not len(list):
        return False
    else:
        return bisect_search_helper(list, elm, 0, len(list)-1)        

# Exponential complexity:
def gen_subsets(list):
    if len(list) == 0:
        return [[]]
    smaller = gen_subsets(list[:-1])
    extra = list[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new


if __name__ == '__main__':
    bisect_search([2, 3, 4, 7, 11], 11)
    bisect_search([2, 3, 4, 7, 11], 10)
    gen_subsets(list(range(4)))