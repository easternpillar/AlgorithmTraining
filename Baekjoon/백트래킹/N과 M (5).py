# Problem:
# Reference: https://www.acmicpc.net/problem/15654

# My Solution:
import sys


def backtrack(start, cnt, visited):
    if cnt == M:
        print(*visited)

    for num in nums:
        if num in visited:
            continue
        temp = visited[:]
        temp.append(num)
        backtrack(num, cnt + 1, temp)


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

for num in nums:
    backtrack(num, 1, [num])

