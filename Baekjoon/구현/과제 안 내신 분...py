# Problem:
# Reference: https://www.acmicpc.net/problem/5597

# My Solution:
import sys

entire = set([i for i in range(1, 31)])
submitted = set([int(sys.stdin.readline().rstrip()) for _ in range(28)])
no = list(entire.difference(submitted))
for n in sorted(no):
    print(n)
