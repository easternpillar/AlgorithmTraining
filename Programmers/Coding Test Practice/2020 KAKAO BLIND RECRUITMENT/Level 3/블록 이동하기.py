# Problem:
# Given a board with a robot that takes two spaces, return the minimum movement to the destination(N, N).
# Condition(s):
# 1. The robot can move up, down, right and left at once.
# 2. The robot can rotate at once.

# My Solution:
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
c = []


def bfs(r, b, m, n):
    q.append(r)
    c.append(r)
    cnt = 0
    while q:
        qlen = len(q)
        while qlen:
            x = q.popleft()
            if x == [[m - 1, n - 2], [m - 1, n - 1]] or x == [[m - 2, n - 1], [m - 1, n - 1]]:
                return cnt
            for i in range(4):
                temp = []
                flag = 0
                for j in range(2):
                    nx = x[j][0] + dx[i]
                    ny = x[j][1] + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and b[nx][ny] == 0:
                        temp.append([nx, ny])
                    else:
                        flag = 1
                        break
                if not flag:
                    if x[0][0] == x[1][0]:
                        if i == 0 or i == 1:
                            turn(x, i, '|')
                    elif x[0][1] == x[1][1]:
                        if i == 2 or i == 3:
                            turn(x, i, '-')
                    temp.sort()
                    if temp not in c:
                        q.append(temp)
                        c.append(temp)
            qlen -= 1
        cnt += 1


def turn(x, i, mode):
    if mode == '|':
        for j in range(2):
            nx = x[j]
            ny = [x[j][0] + dx[i], x[j][1]]
            temp = [nx, ny]
            temp.sort()
            if temp not in c:
                q.append(temp)
                c.append(temp)

    elif mode == '-':
        for j in range(2):
            nx = [x[j][0], x[j][1] + dy[i]]
            ny = x[j]
            temp = [nx, ny]
            temp.sort()
            if temp not in c:
                q.append(temp)
                c.append(temp)


def solution(board):
    m, n = len(board), len(board[0])
    robot = [[0, 0], [0, 1]]
    return bfs(robot, board, m, n)
