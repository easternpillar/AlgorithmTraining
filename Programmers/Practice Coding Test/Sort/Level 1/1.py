# Problem:
# Given an array with 3 elements, return k-th numbers.
# Condition(s):
# 1. First 2 elements mean the range of slicing.
# 2. Third element means the number of k-th after sorting.

# My Solution:
def solution(array, commands):
    answer = []

    for command in commands:
        temp = array[command[0] - 1:command[1]].copy()
        temp.sort()
        answer.extend([temp[command[2] - 1]])
    return answer
