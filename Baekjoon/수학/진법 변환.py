# Problem:
# Given a base B number N, print the number converted to base 10.

# My Solution:
import sys

N, B = sys.stdin.readline().split()
print(int(N, int(B)))