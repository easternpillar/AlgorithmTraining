# Problem:
# Reference: https://www.acmicpc.net/problem/17144

# My Solution:
import sys


def spread():
    temp = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            cnt = 0
            if (i, j) in pos:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in pos:
                    temp[nx][ny] += A[i][j] // 5
                    cnt += 1
            A[i][j] -= (A[i][j] // 5) * cnt

    for i in range(R):
        for j in range(C):
            A[i][j] += temp[i][j]


def circulation():
    cir1, cir2 = pos[0], pos[1]

    row, col = cir1[0], cir1[1]
    prev = -1
    while col < C - 1:
        col += 1
        if prev == -1:
            prev = A[row][col]
            A[row][col] = 0
        else:
            A[row][col], prev = prev, A[row][col]

    while row > 0:
        row -= 1
        if prev == -1:
            prev = A[row][col]
            A[row][col] = 0
        else:
            A[row][col], prev = prev, A[row][col]

    while col > 0:
        col -= 1
        if prev == -1:
            prev = A[row][col]
            A[row][col] = 0
        else:
            A[row][col], prev = prev, A[row][col]

    while row < cir1[0] - 1:
        row += 1
        if prev == -1:
            prev = A[row][col]
            A[row][col] = 0
        else:
            A[row][col], prev = prev, A[row][col]
    A[cir1[0]][cir1[1]] = -1

    row, col = cir2[0], cir2[1]
    prev = -1
    while col < C - 1:
        col += 1
        if prev == -1:
            prev = A[row][col]
            A[row][col] = 0
        else:
            A[row][col], prev = prev, A[row][col]

    while row < R - 1:
        row += 1
        if prev == -1:
            prev = A[row][col]
            A[row][col] = 0
        else:
            A[row][col], prev = prev, A[row][col]

    while col > 0:
        col -= 1
        if prev == -1:
            prev = A[row][col]
            A[row][col] = 0
        else:
            A[row][col], prev = prev, A[row][col]

    while row > cir2[0] - 1:
        row -= 1
        if prev == -1:
            prev = A[row][col]
            A[row][col] = 0
        else:
            A[row][col], prev = prev, A[row][col]

    A[cir1[0]][cir1[1]] = -1
    A[cir2[0]][cir2[1]] = -1


dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

R, C, T = map(int, sys.stdin.readline().split())
A = []
for _ in range(R):
    A.append(list(map(int, sys.stdin.readline().split())))

pos = []
for idx in range(R):
    if A[idx][0] == -1:
        pos.append((idx, 0))

time = 0
while time < T:
    spread()
    circulation()
    time += 1

answer = 0
for a in A:
    answer += sum(a)

print(answer + 2)
