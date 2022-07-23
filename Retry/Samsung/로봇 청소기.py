# Reference: https://www.acmicpc.net/problem/14503
import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
room = []
for _ in range(N):
    room.append(list(map(int, sys.stdin.readline().split())))
answer = 0
cnt = 0

while True:
    if cnt == 4:
        if d == 0:
            if room[r + 1][c] != 1:
                r += 1
            else:
                break
        elif d == 1:
            if room[r][c - 1] != 1:
                c -= 1
            else:
                break
        elif d == 2:
            if room[r - 1][c] != 1:
                r -= 1
            else:
                break
        elif d == 3:
            if room[r][c + 1] != 1:
                c += 1
            else:
                break
        cnt = 0

    if room[r][c] == 0:
        room[r][c] = 2
        answer += 1

    if d == 0:
        if room[r][c - 1] == 0:
            c -= 1
            cnt = 0
        else:
            cnt += 1
        d = 3
    elif d == 1:
        if room[r - 1][c] == 0:
            r -= 1
            cnt = 0
        else:
            cnt += 1
        d = 0
    elif d == 2:
        if room[r][c + 1] == 0:
            c += 1
            cnt = 0
        else:
            cnt += 1
        d = 1
    elif d == 3:
        if room[r + 1][c] == 0:
            r += 1
            cnt = 0
        else:
            cnt += 1
        d = 2
print(answer)
