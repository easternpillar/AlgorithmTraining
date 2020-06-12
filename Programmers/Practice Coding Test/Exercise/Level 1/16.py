# Problem:
# Return the even-numbered alphabet of each word to capital letters and the odd-numbered alphabet to lower-case letters.
# Condition(s):
# 1. Blank means a new string.

# My Solution:
def solution(s):
    answer = ''
    cnt = 0

    for c in s:
        if c == ' ':
            cnt = 0
            answer += c
            continue
        elif cnt % 2 == 0:
            answer += c.upper()
        else:
            answer += c.lower()
        cnt += 1
    return answer

# Learned:
# 1. .upper(), .lower(): converts the case of alphabet.