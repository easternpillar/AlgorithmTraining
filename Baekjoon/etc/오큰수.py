# Problem:
# Given the numbers, print the each leftmost number that is greater than itself from the right of itself.
# Condition(s):
# 1. Print -1 if it does not exist.

# My Solution:
import sys

n = int(sys.stdin.readline())
eli = list(map(int, sys.stdin.readline().rstrip().split()))
answer = [-1 for _ in range(n)]

for i in range(n - 2, -1, -1):
    if eli[i] < eli[i + 1]:
        answer[i] = i + 1
    else:
        tidx = answer[i + 1]
        if tidx == -1:
            continue
        else:
            while True:
                if eli[tidx] == -1:
                    break
                if eli[i] < eli[tidx]:
                    answer[i] = tidx
                    break
                else:
                    if tidx == -1:
                        break
                    tidx = answer[tidx]

for i in answer:
    if i == -1:
        print(i)
    else:
        print(eli[i])
