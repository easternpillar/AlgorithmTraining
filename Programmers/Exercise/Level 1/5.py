# Problem:
# Given 2 numbers, return the sum of number between them.

# My Solution:
def solution(a, b):
    answer = 0

    if a > b:
        for i in range(b, a):
            answer += i
        answer += a
    else:
        for i in range(a, b):
            answer += i
        answer += b
    return answer
