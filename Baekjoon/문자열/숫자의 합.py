# Problem:
# Reference: https://www.acmicpc.net/problem/11720

# My Solution:
import sys

N = sys.stdin.readline().rstrip()
print(sum((map(int, list(sys.stdin.readline().rstrip())))))
