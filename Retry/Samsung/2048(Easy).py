# Reference: https://www.acmicpc.net/problem/12100
import sys
from collections import deque
from copy import deepcopy

N = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque([])
q.append((0, board))


def up(board):
    length = len(board)
    modified = [[False for _ in range(length)] for _ in range(length)]
    for i in range(1, length):
        for j in range(length):
            if board[i][j] != 0:
                original = board[i][j]
                board[i][j] = 0
                idx = 0
                for k in range(i-1, -1, -1):
                    if board[k][j] != 0:
                        idx = k
                        break
                if board[idx][j] == original:
                    if not modified[idx][j]:
                        board[idx][j] *= 2
                        modified[idx][j] = True
                    else:
                        board[idx + 1][j] = original
                else:
                    if board[idx][j] == 0:
                        board[idx][j] = original
                    else:
                        board[idx + 1][j] = original
    return board


def down(board):
    length = len(board)
    modified = [[False for _ in range(length)] for _ in range(length)]
    for i in range(length - 2, -1, -1):
        for j in range(length):
            if board[i][j] != 0:
                original = board[i][j]
                board[i][j] = 0
                idx = length-1
                for k in range(i+1, length, 1):
                    if board[k][j] != 0:
                        idx = k
                        break
                if board[idx][j] == original:
                    if not modified[idx][j]:
                        board[idx][j] *= 2
                        modified[idx][j] = True
                    else:
                        board[idx - 1][j] = original
                else:
                    if board[idx][j] == 0:
                        board[idx][j] = original
                    else:
                        board[idx - 1][j] = original
    return board


def left(board):
    length = len(board)
    modified = [[False for _ in range(length)] for _ in range(length)]
    for i in range(1, length):
        for j in range(length):
            if board[j][i] != 0:
                original = board[j][i]
                board[j][i] = 0
                idx = 0
                for k in range(i-1, -1, -1):
                    if board[j][k] != 0:
                        idx = k
                        break
                if board[j][idx] == original:
                    if not modified[j][idx]:
                        board[j][idx] *= 2
                        modified[j][idx] = True
                    else:
                        board[j][idx + 1] = original
                else:
                    if board[j][idx] == 0:
                        board[j][idx] = original
                    else:
                        board[j][idx + 1] = original
    return board


def right(board):
    length = len(board)
    modified = [[False for _ in range(length)] for _ in range(length)]
    for i in range(length - 2, -1, -1):
        for j in range(length):
            if board[j][i] != 0:
                original = board[j][i]
                board[j][i] = 0
                idx = length-1
                for k in range(i+1, length, 1):
                    if board[j][k] != 0:
                        idx = k
                        break
                if board[j][idx] == original:
                    if not modified[j][idx]:
                        board[j][idx] *= 2
                        modified[j][idx] = True
                    else:
                        board[j][idx - 1] = original
                else:
                    if board[j][idx] == 0:
                        board[j][idx] = original
                    else:
                        board[j][idx - 1] = original
    return board


maxi = 0
while q:
    cnt, board = q.popleft()
    # print(cnt)
    # for b in board:
    #     print(b)
    if cnt > 5:
        continue

    for b in board:
        maxi = max(maxi, max(b))

    q.append((cnt + 1, up(deepcopy(board))))
    q.append((cnt + 1, down(deepcopy(board))))
    q.append((cnt + 1, left(deepcopy(board))))
    q.append((cnt + 1, right(deepcopy(board))))

print(maxi)
