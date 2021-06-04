# Problem:
# Reference: https://www.acmicpc.net/problem/18222

# My Solution:
import sys


def recursive(nth):
    if nth == 0:
        return 0
    else:
        cnt = 0
        while nth > 0:
            mul = 0
            while nth >= 2 ** mul:
                mul += 1
            mul -= 1
            nth = nth - 2 ** mul
            cnt += 1

        if cnt == 1:
            return 1
        else:
            if cnt % 2 == 0:
                return 0
            else:
                return 1


X = "0"
k = int(sys.stdin.readline().rstrip())
print(recursive(k - 1))
