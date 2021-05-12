# Problem:
# Given two natural numbers N and M, print the sequences of length M selected without duplicates from 1 to N.

# My Solution:
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
for comb in combinations([i for i in range(1, N + 1)], M):
    for c in comb:
        print(c, end=" ")
    print()
