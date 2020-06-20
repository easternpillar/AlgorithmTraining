# Problem:
# Given a natural number, return the number of ways to express the number in successive natural numbers.

# My Solution:
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        tot = i
        while tot < n:
            i += 1
            tot += i
        if tot == n:
            answer += 1

    return answer
