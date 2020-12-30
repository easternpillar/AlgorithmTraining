# Problem:
# Given two strings of numbers, print the maximum sum of the products of the numbers facing each other.

# My Solution:
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    long = list(map(int, input().split()))
    short = list(map(int, input().split()))
    print("#{}".format(i + 1), end=" ")

    if len(long) < len(short):
        long, short = short, long

    maximum = 0
    for j in range(len(long) - len(short) + 1):
        total = 0
        for k in range(len(short)):
            total += short[k] * long[j + k]
        if total > maximum:
            maximum = total

    print(maximum)
