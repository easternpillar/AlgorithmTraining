# Problem:
# Reference: https://www.acmicpc.net/problem/15721

# My Solution:
import sys

A = int(sys.stdin.readline().rstrip())
T = int(sys.stdin.readline().rstrip())
flag = int(sys.stdin.readline().rstrip())

idxs = [[], []]

idx = -1
cycle = 1
while True:
    for _ in range(2):
        idx += 1
        idxs[0].append(idx)
        idx += 1
        idxs[1].append(idx)
    for _ in range(cycle+1):
        idx += 1
        idxs[0].append(idx)
    for _ in range(cycle+1):
        idx += 1
        idxs[1].append(idx)
    cycle += 1

    if flag == 0:
        if len(idxs[0]) >= T:
            print((idxs[0][T - 1]) % A)
            break
    elif flag == 1:
        if len(idxs[1]) >= T:
            print((idxs[1][T - 1]) % A)
            break
