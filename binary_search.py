"""
binary search
"""

# no recursive implementation


def binary_search(alist, item):
    # initialization
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if item == alist[mid]:
           found = True
        elif item > alist[mid]:
            first = mid + 1
        else:
            last = mid - 1

    return found

# recursive implementation
def binary_search_recurive(alist, item):
    # divide and counquer
    # initial condition
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binary_search_recurive(alist[:mid])
            else:
                return binary_search_recurive(alist[mid:])
