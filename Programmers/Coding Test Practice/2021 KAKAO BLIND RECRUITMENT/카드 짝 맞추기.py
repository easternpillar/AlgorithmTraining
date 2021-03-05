# Problem:
# Reference: https://programmers.co.kr/learn/courses/30/lessons/72415

# My Solution:
from itertools import permutations
from collections import deque

size = 4
myboard = [[] for i in range(4)]
card_pos = {}
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
INF = int(1e4)
answer = INF
orders = []


def init(board):
    global myboard, card_pos, orders
    for i in range(size):
        for j in range(size):
            if board[i][j] != 0:
                card = board[i][j]
                if card not in card_pos.keys():
                    card_pos[card] = [[i, j]]
                else:
                    card_pos[card].append([i, j])

            myboard[i].append(board[i][j])

    orders = [key for key in card_pos.keys()]
    orders = list(permutations(orders))


def isin(y, x):
    if -1 < y < size:
        if -1 < x < size: return True

    return False


def move(y, x, mv):
    global myboard
    ny, nx = y, x

    while True:
        _ny = ny + mv[0]
        _nx = nx + mv[1]
        if not isin(_ny, _nx): return ny, nx
        if myboard[_ny][_nx] != 0: return _ny, _nx

        ny = _ny
        nx = _nx


def bfs(sy, sx, ey, ex):
    if [sy, sx] == [ey, ex]: return sy, sx, 1
    global myboard
    q = []
    q = deque(q)
    table = [[0 for j in range(size)] for i in range(size)]
    visit = [[False for j in range(size)] for i in range(size)]
    q.append([sy, sx])
    visit[sy][sx] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            if isin(ny, nx):
                if not visit[ny][nx]:
                    visit[ny][nx] = True
                    table[ny][nx] = table[y][x] + 1
                    if [ny, nx] == [ey, ex]:
                        return ny, nx, table[ny][nx] + 1

                    q.append([ny, nx])

            ny, nx = move(y, x, d[i])

            if not visit[ny][nx]:
                visit[ny][nx] = True
                table[ny][nx] = table[y][x] + 1
                if [ny, nx] == [ey, ex]:
                    return ny, nx, table[ny][nx] + 1

                q.append([ny, nx])

    return sy, sx, INF


def remove(card):
    global myboard, card_pos
    for y, x in card_pos[card]: myboard[y][x] = 0


def restore(card):
    global myboard, card_pos
    for y, x in card_pos[card]: myboard[y][x] = card


def backtrack(sy, sx, k, m, count):
    global orders, myboard, answer, card_pos

    if k == len(card_pos.keys()):
        if answer > count: answer = count
        return

    card = orders[m][k]
    left_y, left_x = card_pos[card][0][0], card_pos[card][0][1]
    right_y, right_x = card_pos[card][1][0], card_pos[card][1][1]

    ry1, rx1, res1 = bfs(sy, sx, left_y, left_x)
    ry2, rx2, res2 = bfs(ry1, rx1, right_y, right_x)

    remove(card)
    backtrack(ry2, rx2, k + 1, m, count + res1 + res2)
    restore(card)

    ry1, rx1, res1 = bfs(sy, sx, right_y, right_x)
    ry2, rx2, res2 = bfs(ry1, rx1, left_y, left_x)

    remove(card)
    backtrack(ry2, rx2, k + 1, m, count + res1 + res2)
    restore(card)


def solution(board, r, c):
    global answer
    init(board)

    for i in range(len(orders)):
        backtrack(r, c, 0, i, 0)

    return answer