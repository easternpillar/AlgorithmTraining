# Problem:
# Given a string with numbers, return the string consisting of the minimum value and the maximum value.

# My Solution:
def solution(s):
    s = s.split()
    s = list(map(int, s))
    answer = str(min(s)) + ' ' + str(max(s))
    return answer
