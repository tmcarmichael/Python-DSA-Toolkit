# Example of two-pointers pattern

def twoPointer(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        if target > current_sum:
            left += 1
        else:
            right -= 1
    return [-1, -1]