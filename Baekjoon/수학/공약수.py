# Problem:
# Given the numbers, print the divisors.

# My Solution:
import sys


def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return abs(a)


answer = []
n = int(sys.stdin.readline().rstrip())
naturals = list(map(int, sys.stdin.readline().split()))
minimum = min(naturals)
g = 0
if len(naturals) == 2:
    g = gcd(naturals[0], naturals[1])
else:
    g = gcd(gcd(naturals[0], naturals[1]), naturals[2])

for i in range(1, int(g ** 0.5) + 1, 1):
    if g % i == 0:
        answer.append(i)
        answer.append(int(g / i))

for a in list(sorted(list(set(sorted(answer))))):
    print(a)
