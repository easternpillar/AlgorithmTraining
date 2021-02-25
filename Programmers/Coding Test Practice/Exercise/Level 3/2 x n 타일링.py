# Problem:
# Given the length of a rectangle's width, return the number of ways to fill this rectangle.

# My Solution:
def solution(n):
    li = [0 for i in range(60000)]
    li[1] = 1
    li[2] = 2

    for i in range(3, n + 1):
        li[i] = (li[i - 1] + li[i - 2]) % 1000000007

    answer = li[n]
    return answer
