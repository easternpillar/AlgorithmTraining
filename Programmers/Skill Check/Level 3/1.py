# Problem:
# Given the number of persons, return the k-th case in a dictionary arrangement.

# My Solution:
def factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact


def solution(n, k):
    answer = []
    num = [i + 1 for i in range(n)]

    while n > 0:
        fact = factorial(n - 1)
        answer.extend([num[(k - 1) // fact]])
        num.pop((k - 1) // fact)
        k = k % factorial(n - 1)
        n -= 1
    return answer
