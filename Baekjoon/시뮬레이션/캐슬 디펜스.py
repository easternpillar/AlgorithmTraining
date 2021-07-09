# Problem:
# Reference: https://www.acmicpc.net/problem/17135

# My Solution:
import copy
import math
import sys
from itertools import combinations


def target(c, enemy):
    rList = []
    for col in c:

        prev = math.inf
        tList = []
        for e in enemy:
            distance = abs(e[0] - N) + abs(e[1] - col)
            if distance == prev:
                tList.append((distance, e))
                continue
            if prev > distance and distance <= D:
                prev = distance
                tList = [(distance, e)]

        if tList:
            tList.sort(key=lambda x: (x[0], x[1][1]))
            rList.append(tList[0][1])
    return rList


def play(comb, enemy):
    cnt = 0
    while enemy:
        removes = target(comb, enemy)
        removes = set(map(tuple, removes))

        for remove in removes:
            if list(remove) in enemy:
                enemy.remove(list(remove))
                cnt += 1

        for e in enemy:
            e[0] += 1
        enemy = [e for e in enemy if e[0] < N]
    return cnt


N, M, D = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
enemies = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            enemies.append([i, j])

answer = 0
for comb in combinations([i for i in range(M)], 3):
    answer = max(answer, play(comb, copy.deepcopy(enemies)))

print(answer)
