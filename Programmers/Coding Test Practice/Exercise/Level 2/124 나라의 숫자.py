# Problem:
# Given a number, return the value that changed n to the number used in 124 countries.

# My Solution:
def solution(n):
    answer = ''
    while n != 0:
        n -= 1
        q, r = divmod(n, 3)
        n = q
        answer = "124"[r] + answer

    return answer
