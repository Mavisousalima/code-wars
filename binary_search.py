"""
implement a binary search algorithm that can quickly search for a specific value in a sorted list of numbers

Return the index of the location in the array or -1 if the array did not contain the target value
"""


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(binary_search([1, 2, 3, 4], 4))
print(binary_search([1, 2, 3], 3))
