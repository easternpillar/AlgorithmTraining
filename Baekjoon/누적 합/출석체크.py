# Problem:
# Reference: https://www.acmicpc.net/problem/20438

# My Solution:
import sys

N, K, Q, M = map(int, (sys.stdin.readline().split()))
students = [False for _ in range(N + 3)]

ks = list(map(int, sys.stdin.readline().split()))

for q in map(int, sys.stdin.readline().split()):
    if q in ks:
        continue

    for num in range(q, N + 3, q):
        if num in ks:
            continue
        else:
            students[num] = True

sums = [0 for _ in range(len(students))]

for i in range(1, len(students)):
    if not students[i]:
        sums[i] += sums[i - 1] + 1
    else:
        sums[i] = sums[i - 1]

for _ in range(M):
    f, t = map(int, sys.stdin.readline().split())
    print(sums[t] - sums[f - 1])
