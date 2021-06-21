# Problem:
# Reference: https://www.acmicpc.net/problem/15652

# My Solution:
import sys


def backtrack(sequence):
    if len(sequence) == M:
        print(*sequence)
        return

    for i in range(sequence[-1], N + 1):
        temp = sequence[:]
        temp.append(i)
        backtrack(temp)


N, M = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, N + 1)]
for i in range(1, N + 1):
    backtrack([i])
