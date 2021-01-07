# Problem:
# Given the height of the wires connected between the two poles, print the number of wire crossings.
# Condition(s):
# 1. Three or more wires do not meet at one point.

# My Solution:
TC = int(input())
for i in range(TC):
    N = int(input())

    dots = []
    cnt = 0
    for j in range(N):
        a, b = map(int, input().split())
        for c_a, c_b in dots:
            if (a > c_a and b < c_b) or (a < c_a and b > c_b):
                cnt += 1
        dots.append((a, b))

    print("#{} {}".format(i + 1, cnt))
