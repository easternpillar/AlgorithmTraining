# Problem:
# Return the array that stores the integer, the array that removes the smallest number from arr.
# Condition(s):
# 1. If arr becomes empty, return [-1].

# My Solution:
def solution(arr):
    arr.remove(min(arr))
    if not arr:
        arr.append(-1)

    return arr
