# Problem:
# Given a string of a decimal number, print the string sorted in descending order.

# My Solution:
def solution(n):
    answer = 0
    answer = str(n)
    answer = list(answer)
    answer.sort()
    answer.reverse()
    answer = "".join(answer)
    answer = int(answer)
    return answer

# Learned:
# 1. (token).join(list): merge the elements in list by join criteria.
