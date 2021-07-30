# Problem:
# Reference: https://www.acmicpc.net/problem/2512

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
budgets = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
left = 0
right = max(budgets)
answer = []
while True:
    if left > right:
        break

    mid = (left + right) // 2
    tot = 0
    for i in range(N):
        if budgets[i] - mid < 0:
            tot += budgets[i]
        else:
            tot += mid
    if tot > M:
        right = mid - 1
    elif tot <= M:
        answer.append(mid)
        left = mid + 1
    else:
        break
print(max(answer))
