# Problem:
# Reference: https://www.acmicpc.net/problem/2805

# My Solution:
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
l = 0
r = max(trees)

result = []
while not r < l:
    length = 0
    mid = (l + r) // 2
    length = sum(i - mid if i > mid else 0 for i in trees)

    if length == M:
        result.append(mid)
        break
    elif length > M:
        result.append(mid)
        l = mid + 1
    else:
        r = mid - 1

print(max(result))
