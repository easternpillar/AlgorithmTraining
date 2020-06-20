# Problem:
# Convert a string into a integer.
# Condition(s):
# Signs can come at the beginning of a string.

# My Solution:
def solution(s):
    if s[0] == '+':
        answer = int(s[1:])
    elif s[0] == '-':
        answer = -int(s[1:])
    else:
        answer = int(s)
    return answer
