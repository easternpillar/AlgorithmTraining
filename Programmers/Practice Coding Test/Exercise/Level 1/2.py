# Problem:
# Given a string, return the middle character.
# Condition:
# 1. If the length of string is even number, return 2 characters.

# My Solution:
def solution(s):
    length = len(s)
    if length % 2 == 0:
        answer = s[length // 2 - 1:length // 2 + 1]
    else:
        answer = s[length // 2]
    return answer
