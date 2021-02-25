# Problem:
# If you can move 1 or 2 spaces at a time, return the number of ways to reach n spaces.

# My Solution:
def solution(n):
    li = [0 for i in range(n + 1)]
    li[0] = 1
    li[1] = 2
    for i in range(2, len(li)):
        li[i] = li[i - 2] + li[i - 1]

    return li[n - 1] % 1234567
