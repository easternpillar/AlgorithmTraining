# Reference: https://www.acmicpc.net/problem/15686
import math
import sys
from itertools import combinations


def distance(h, s):
    return abs(h[0] - s[0]) + abs(h[1] - s[1])


N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
houses = []
stores = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            stores.append((i, j))
to_close = len(stores) - M

if to_close <= 0:
    answer = 0
    for h in houses:
        mini = math.inf
        for s in stores:
            mini = min(distance(h, s), mini)
        answer += mini
    print(answer)
else:
    answer = math.inf
    for comb in combinations(stores, to_close):
        temp = 0
        for h in houses:
            mini = math.inf
            for s in stores:
                if s in comb:
                    continue
                mini = min(distance(h, s), mini)
            temp += mini
        answer = min(answer, temp)
    print(answer)
