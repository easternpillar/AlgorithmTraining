# Problem:
# Reference: https://www.acmicpc.net/problem/22864

# My Solution:
import sys

A, B, C, M = map(int, sys.stdin.readline().split())
fatigue = 0
work = 0
rest = 0
answer = 0
while True:
    if A > M:
        break
    while fatigue + A > M:
        rest += 1
        fatigue -= C
        if work + rest == 24:
            break
        if fatigue < 0:
            fatigue = 0
    if work + rest == 24:
        break
    work += 1
    answer += B
    fatigue += A

print(answer)
