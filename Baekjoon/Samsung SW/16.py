# Problem:
# Given dragon curves, return the number of four vertices in a square of size 1x1 that are all part of a dragon curve.

# My Solution:
N = int(input())
map_data = [[1] * 101 for _ in range(101)]
di = {0: [0, 1], 1: [-1, 0], 2: [0, -1], 3: [1, 0]}
for _ in range(N):
    x, y, d, g, = map(int, input().split())

    curve_info = [d]
    for _ in range(g):
        curve_info += [(i + 1) % 4 for i in curve_info[::-1]]
    map_data[y][x] = 0
    nx = x
    ny = y
    for curve in curve_info:
        nx = nx + di[curve][1]
        ny = ny + di[curve][0]
        map_data[ny][nx] = 0

# 정답 구하기
cnt = 0
for i in range(100):
    for j in range(100):
        if map_data[i][j] + map_data[i][j + 1] + map_data[i + 1][j] + map_data[i + 1][j + 1] == 0:
            cnt += 1
print(cnt)
