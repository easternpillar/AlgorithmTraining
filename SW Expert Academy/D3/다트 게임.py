# Problem:
# Given a dartboard with 10 circles in 20mm increments and the coordinates of each dart, print the total score.
# Condition(s):
# 1. Score from 1 to 10 points from the outermost circle to the innermost circle.

# My Solution: DENIED.
import math

TC = int(input())

for i in range(TC):
    N = int(input())
    tot = 0
    print("#{}".format(i + 1), end=" ")
    for j in range(N):
        x, y = map(int, input().split())
        r = math.sqrt(math.pow(x,2)+math.pow(y,2))

        for c in range(0, 11, 1):
            if c * 20 < r <= (c + 1) * 20:
                tot += 10 - c

    print(tot)
