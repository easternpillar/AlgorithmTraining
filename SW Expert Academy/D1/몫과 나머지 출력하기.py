# Problem:
# Given two numbers, print the quotient and the remainder.

# My Solution:
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print("#{} {} {}".format(i + 1, *divmod(a, b)))
