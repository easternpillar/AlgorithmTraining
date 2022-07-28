# Reference: https://www.acmicpc.net/problem/15683
import math
import sys
from copy import deepcopy

N, M = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cctvs = []

for i in range(N):
    for j in range(M):
        if room[i][j] != 0 and room[i][j] != 6:
            cctvs.append((i, j, room[i][j]))

answer = math.inf


def monitor(room, directions):
    global cctvs
    room_copied = deepcopy(room)
    for i in range(len(cctvs)):
        direction = directions[i]
        type = cctvs[i][2]
        x, y = cctvs[i][0], cctvs[i][1]
        if type == 1:
            if direction == 0:
                for j in range(y + 1, M, 1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
            elif direction == 1:
                for j in range(y - 1, -1, -1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
            elif direction == 2:
                for j in range(x + 1, N, 1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
            elif direction == 3:
                for j in range(x - 1, -1, -1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
        elif type == 2:
            if direction == 0 or direction == 1:
                for j in range(y + 1, M, 1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
                for j in range(y - 1, -1, -1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
            elif direction == 2 or direction == 3:
                for j in range(x + 1, N, 1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
                for j in range(x - 1, -1, -1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
        elif type == 3:
            if direction == 0:
                for j in range(y + 1, M, 1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
                for j in range(x - 1, -1, -1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
            elif direction == 1:
                for j in range(y + 1, M, 1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
                for j in range(x + 1, N, 1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
            elif direction == 2:
                for j in range(x + 1, N, 1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
                for j in range(y - 1, -1, -1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
            elif direction == 3:
                for j in range(y - 1, -1, -1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
                for j in range(x - 1, -1, -1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
        elif type == 4:
            if direction == 0:
                for j in range(y - 1, -1, -1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
                for j in range(x - 1, -1, -1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
                for j in range(y + 1, M, 1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
            elif direction == 1:
                for j in range(x - 1, -1, -1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
                for j in range(y + 1, M, 1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
                for j in range(x + 1, N, 1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
            elif direction == 2:
                for j in range(y + 1, M, 1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
                for j in range(x + 1, N, 1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
                for j in range(y - 1, -1, -1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
            elif direction == 3:
                for j in range(x + 1, N, 1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
                for j in range(y - 1, -1, -1):
                    if room_copied[x][j] == 6:
                        break
                    if room_copied[x][j] != 0:
                        continue
                    room_copied[x][j] = '#'
                for j in range(x - 1, -1, -1):
                    if room_copied[j][y] == 6:
                        break
                    if room_copied[j][y] != 0:
                        continue
                    room_copied[j][y] = '#'
        elif type == 5:
            for j in range(x + 1, N, 1):
                if room_copied[j][y] == 6:
                    break
                if room_copied[j][y] != 0:
                    continue
                room_copied[j][y] = '#'
            for j in range(y - 1, -1, -1):
                if room_copied[x][j] == 6:
                    break
                if room_copied[x][j] != 0:
                    continue
                room_copied[x][j] = '#'
            for j in range(x - 1, -1, -1):
                if room_copied[j][y] == 6:
                    break
                if room_copied[j][y] != 0:
                    continue
                room_copied[j][y] = '#'
            for j in range(y + 1, M, 1):
                if room_copied[x][j] == 6:
                    break
                if room_copied[x][j] != 0:
                    continue
                room_copied[x][j] = '#'
    cnt = 0
    for i in range(len(room_copied)):
        for j in range(len(room_copied[0])):
            if room_copied[i][j] == 0:
                cnt += 1
    return cnt


def dfs(depth, limit, directions, room):
    global answer
    if depth == limit:
        answer = min(monitor(room, directions), answer)
        return

    for i in range(4):
        directions_copied = directions[:]
        directions_copied.append(i)
        dfs(depth + 1, limit, directions_copied, room)


dfs(0, len(cctvs), [], room)
print(answer)
