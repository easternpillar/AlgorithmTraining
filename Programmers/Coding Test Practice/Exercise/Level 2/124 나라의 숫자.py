# Problem:
# Given a number, return the value that changed n to the number used in 124 countries.

# My Solution:
def solution(n):
    answer = ''
    while n != 0:
        n -= 1
        answer = '124'[n % 3] + answer
        n //= 3
    return answer
