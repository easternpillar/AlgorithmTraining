# Problem:
# Reference: https://www.acmicpc.net/problem/15651

# My Solution:
import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())
for p in product([i for i in range(1, N + 1, 1)], repeat=M):
    print(*p)
