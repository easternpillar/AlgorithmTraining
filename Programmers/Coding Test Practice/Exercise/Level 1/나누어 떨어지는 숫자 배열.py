# Problem:
# Given a list of integers and a divisor, return sorted list that has divided numbers.

# My Solution:
def solution(arr, divisor):
    new_arr = []
    for num in arr:
        if num % divisor == 0:
            new_arr.append(num)
    if not new_arr:
        return [-1]
    else:
        new_arr.sort()
        return new_arr
