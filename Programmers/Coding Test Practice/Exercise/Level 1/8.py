# Problem:
# Given a string, return sorted string by descending order.

# My Solution:
def solution(s):
    s = list(s)
    s.sort(key=lambda x: -ord(x))
    s = "".join(s)
    return s
