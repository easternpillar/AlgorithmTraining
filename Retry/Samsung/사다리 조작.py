# Reference: https://www.acmicpc.net/problem/15684
import math
import sys


def dfs(horizons, cnt, idx):
    start_i, start_j = idx[0], idx[1]
    global answer
    if cnt > 3:
        return
    if play(horizons):
        answer = min(answer, cnt)
        return

    for i in range(start_i, H + 1):
        for j in range(1, N):
            if i == start_i and j < start_j:
                continue
            if not horizons[i][j]:
                if not horizons[i][j - 1] and not horizons[i][j + 1]:
                    horizons[i][j] = True
                    dfs(horizons, cnt + 1, (i, j))
                    horizons[i][j] = False


def play(horizons):
    for i in range(1, len(horizons[0]) - 1):
        col = i
        row = 1
        while row < len(horizons) - 1:
            if horizons[row][col]:
                col += 1
            elif horizons[row][col - 1]:
                col -= 1
            row += 1
        if i != col:
            return False
    return True


N, M, H = map(int, sys.stdin.readline().split())
horizons = [[False for _ in range(N + 1)] for _ in range(H + 2)]
answer = math.inf
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    horizons[a][b] = True

dfs(horizons, 0, (1, 1))
if answer == math.inf:
    print(-1)
else:
    print(answer)
