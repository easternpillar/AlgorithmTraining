# Problem:
# Given two natural numbers, print the LCM.

# My Solution:
import sys
import math

for _ in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    gcd = math.gcd(a, b)
    print(a // gcd * b // gcd * gcd)
