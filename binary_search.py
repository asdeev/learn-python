"""
Author: Zaid Bhura
Description: Binary Search Algorithm
"""


def binary_search(arr, num):
    low = 0
    high = len(arr) - 1

    found = False
    index = -1

    while low <= high and not found:
        mid = (low + high) // 2

        if arr[mid] == num:
            index = mid
            found = True
        else:
            if arr[mid] < num:
                low = mid + 1
            elif arr[mid] > num:
                high = mid - 1
    return index


values = [5,7,7,8,8,8,8,8,8,8,10]
target = 8

found_index = binary_search(values, target)
print(found_index)
