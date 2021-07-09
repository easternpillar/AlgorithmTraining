# Problem:
# Reference: https://www.acmicpc.net/problem/11265

# My Solution:
import sys


def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])


N, M = map(int, sys.stdin.readline().split())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
floyd()

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    if costs[A - 1][B - 1] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")