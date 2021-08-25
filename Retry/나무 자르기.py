# Problem:
# Reference: https://www.acmicpc.net/problem/2805

# My Solution:
import sys

N, M = map(int, sys.stdin.readline().split())
woods = list(map(int, sys.stdin.readline().split()))
left = 0
right = max(woods)

answer = []
while left <= right:
    mid = (left + right) // 2
    tot = sum(i - mid if i > mid else 0 for i in woods)
    if tot == M:
        answer.append(mid)
        break
    elif tot > M:
        answer.append(mid)
        left = mid + 1
    else:
        right = mid - 1

print(max(answer))
