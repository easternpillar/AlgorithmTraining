# Reference: https://www.acmicpc.net/problem/17144
import sys
from collections import deque

R, C, T = map(int, sys.stdin.readline().split())
rooms = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
dirts = deque([])
cleaner = []
for i in range(R):
    for j in range(C):
        if rooms[i][j] == -1:
            cleaner.append(i)
        elif rooms[i][j] != 0:
            dirts.append((rooms[i][j], i, j))

time = 0
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
while time < T:
    add = []
    while dirts:
        amount, x, y = dirts.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and rooms[nx][ny] != -1:
                add.append((nx, ny, amount // 5))
                cnt += 1
        rooms[x][y] -= cnt * (amount // 5)
    while add:
        x, y, amount = add.pop()
        rooms[x][y] += amount
    for i in range(cleaner[0] - 1, 0, -1):
        rooms[i][0] = rooms[i - 1][0]
    for i in range(0, C - 1, 1):
        rooms[0][i] = rooms[0][i + 1]
    for i in range(0, cleaner[0], 1):
        rooms[i][C - 1] = rooms[i + 1][C - 1]
    for i in range(C - 1, 0, -1):
        rooms[cleaner[0]][i] = rooms[cleaner[0]][i - 1]
    for i in range(cleaner[1] + 1, R - 1, 1):
        rooms[i][0] = rooms[i + 1][0]
    for i in range(0, C - 1, 1):
        rooms[R - 1][i] = rooms[R - 1][i + 1]
    for i in range(R - 1, cleaner[1], -1):
        rooms[i][C - 1] = rooms[i - 1][C - 1]
    for i in range(C - 1, 0, -1):
        rooms[cleaner[1]][i] = rooms[cleaner[1]][i - 1]
    rooms[cleaner[0]][1] = 0
    rooms[cleaner[1]][1] = 0
    time += 1
    for i in range(0, R, 1):
        for j in range(0, C, 1):
            if rooms[i][j] != 0 and rooms[i][j] != -1:
                dirts.append((rooms[i][j], i, j))

answer = 0
for room in rooms:
    answer += sum(room)
print(answer + 2)
