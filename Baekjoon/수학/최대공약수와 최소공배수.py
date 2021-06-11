# Problem:
# Given two natural numbers, print the GCD and LCM.

# My Solution:
import math
import sys

a, b = map(int, sys.stdin.readline().split())
gcd = math.gcd(a, b)
print(gcd)
print(gcd * (a // gcd) * (b // gcd))
