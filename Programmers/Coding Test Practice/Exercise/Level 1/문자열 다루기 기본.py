# Problem:
# Given a string,return False if the length of it is not 4 or 6 and each character is not digit.

# My Solution:
def solution(s):
    answer = True

    if len(s) != 4 and len(s) != 6:
        answer = False

    for ch in s:
        if ord(ch) < 48 or ord(ch) > 57:
            answer = False

    return answer
